using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using NetTopologySuite.IO.Converters;
using NetTopologySuite.Geometries;
using NetTopologySuite.IO;
using DAI.Edit.Models;
using IdentityModel.OidcClient;
using JsonApiSerializer;
using Newtonsoft.Json;
using Serilog;

namespace NetCoreConsoleApp
{
    public class Program
    {
        static readonly string _clientId = "my_client_id";
        static readonly string _host = "http://localhost";
        static readonly int _port = 5001;
        static readonly string _redirectUri = $"{_host}:{_port}/login";
        static readonly string _postLogoutRedirectUri = $"{_host}:{_port}/login";

        static readonly string _authority = "https://log-in.test.miljoeportal.dk/runtime/oauth2";
        static readonly string _scope = "openid http://www.miljoeportal.dk/roles";
        static readonly string _api = "https://arealeditering-v2-api.test.miljoeportal.dk/";

        static OidcClient _oidcClient;
        static HttpClient _apiClient = new HttpClient { BaseAddress = new Uri(_api) };


        public static void Main(string[] args) => MainAsync().GetAwaiter().GetResult();

        public static async Task MainAsync()
        {
            Console.WriteLine("+-----------------------+");
            Console.WriteLine("|  Sign in with OIDC    |");
            Console.WriteLine("+-----------------------+");
            Console.WriteLine("");
            Console.WriteLine("Press any key to sign in...");
            Console.ReadKey();

            await SignInAsync();

            Console.ReadKey();
        }

        private async static Task SignInAsync()
        {
            // create a redirect URI using an available port on the loopback address.
            // requires the OP to allow random ports on 127.0.0.1 - otherwise set a static port

            var browser = new SystemBrowser(_host, _port);

            var options = new OidcClientOptions
            {
                Authority = _authority,
                ClientId = _clientId,
                RedirectUri = _redirectUri,
                Scope = _scope,
                FilterClaims = false,
                Browser = browser,
                PostLogoutRedirectUri = _postLogoutRedirectUri,
                Policy = new Policy() { Discovery = new IdentityModel.Client.DiscoveryPolicy() { ValidateEndpoints = false } }, // Use only for localhost
            };

            var serilog = new LoggerConfiguration()
                .MinimumLevel.Information()
                .Enrich.FromLogContext()
                .WriteTo.LiterateConsole(outputTemplate: "[{Timestamp:HH:mm:ss} {Level}] {SourceContext}{NewLine}{Message}{NewLine}{Exception}{NewLine}")
                .CreateLogger();

            options.LoggerFactory.AddSerilog(serilog);

            _oidcClient = new OidcClient(options);
            var result = await _oidcClient.LoginAsync(new LoginRequest());

            ShowLoginResult(result);

            await TestApi(result);
        }



        #region Login
        private static void ShowLoginResult(LoginResult result)
        {
            if (result.IsError)
            {
                Console.WriteLine("\n\nError:\n{0}", result.Error);
                return;
            }

            Console.WriteLine("\n\nClaims:");
            foreach (var claim in result.User.Claims)
            {
                Console.WriteLine("{0}: {1}", claim.Type, claim.Value);
            }

            Console.WriteLine($"\nidentity token: {result.IdentityToken}");
            Console.WriteLine($"access token:   {result.AccessToken}");
            Console.WriteLine($"refresh token:  {result?.RefreshToken ?? "none"}");

            var values = JsonConvert.DeserializeObject<Dictionary<string, string>>(result.TokenResponse.Raw);

            Console.WriteLine($"Raw TokenResponse ...");
            foreach (var item in values)
            {
                Console.WriteLine($"{item.Key}: {item.Value}");
            }

        }
        #endregion

        #region Test Api
        private static async Task TestApi(LoginResult result)
        {
            HttpResponseMessage response = new HttpResponseMessage();

            var currentAccessToken = result.AccessToken;
            var currentRefreshToken = result.RefreshToken;

            var serializerSettings = new JsonApiSerializerSettings();
            serializerSettings.Converters.Add(new GeometryConverter());
            serializerSettings.Converters.Add(new CoordinateConverter());

            var menu = new StringBuilder();
            menu.Append("Press...\n");
            menu.Append("x -> exit\n");
            menu.Append("k -> list all 'temakoder'\n");
            menu.Append("a -> list all 'attributter'\n");
            menu.Append("t -> list all 'temaattributter'\n");
            menu.Append("o -> list 'objekter'\n");
            menu.Append("p -> create fredede_omr_bk objekt\n\n");
            if (currentRefreshToken != null) menu.Append("r -> refresh token\n");
            menu.Append("c -> logout\n");

            while (true)
            {
                Console.WriteLine("\n\n");
                Console.Write(menu);
                var key = Console.ReadKey();

                if (key.Key == ConsoleKey.X) return;
                if (key.Key == ConsoleKey.K)
                {
                    response = await CallApi("get", currentAccessToken, "temakoder");
                    if (response.IsSuccessStatusCode)
                    {
                        var json = await response.Content.ReadAsStringAsync();
                        var temakoder = JsonConvert.DeserializeObject<List<Temakode>>(json, serializerSettings);
                        WriteTemakoder(temakoder);
                    }
                }
                if (key.Key == ConsoleKey.A)
                {
                    response = await CallApi("get", currentAccessToken, "attributter");
                    if (response.IsSuccessStatusCode)
                    {
                        var json = await response.Content.ReadAsStringAsync();
                        var temaattributter = JsonConvert.DeserializeObject<List<Temaattribut>>(json, serializerSettings);
                        var attributter = temaattributter.ConvertAll(ta => (Attribut)ta);
                        WriteAttributter(attributter);
                    }
                }
                if (key.Key == ConsoleKey.T)
                {
                    response = await CallApi("get", currentAccessToken, "temaattributter");
                    if (response.IsSuccessStatusCode)
                    {
                        var json = await response.Content.ReadAsStringAsync();
                        var temaattributter = JsonConvert.DeserializeObject<List<Attribut>>(json, serializerSettings);
                        WriteAttributter(temaattributter);
                    }
                }
                if (key.Key == ConsoleKey.O)
                {
                    response = await CallApi("get", currentAccessToken, "objekter?intersects=POLYGON ((488884 6114493, 488984 6114493, 488984 6114393, 488884 6114393, 488884 6114493))&filter=any(temakode.id,'2140','2013')&include=temakode");
                    if (response.IsSuccessStatusCode)
                    {
                        var json = await response.Content.ReadAsStringAsync();
                        var objekter = JsonConvert.DeserializeObject<List<Objekter>>(json, serializerSettings);
                        WriteObjekter(objekter);
                    }
                }
                if (key.Key == ConsoleKey.P)
                {
                    var payload = JsonConvert.SerializeObject(CreateObjekt(), serializerSettings);
                    response = await CallApi("post", currentAccessToken, "objekter", payload);
                    if (response.IsSuccessStatusCode)
                    {
                        var responseStr = await response.Content.ReadAsStringAsync();
                        Console.WriteLine("\n");
                        Console.WriteLine($"create new objekt...: {responseStr}");
                    }
                }
                if (key.Key == ConsoleKey.R)
                {
                    var refreshResult = await _oidcClient.RefreshTokenAsync(currentRefreshToken);
                    if (refreshResult.IsError)
                    {
                        Console.WriteLine($"Error: {refreshResult.Error}");
                    }
                    else
                    {
                        currentRefreshToken = refreshResult.RefreshToken;
                        currentAccessToken = refreshResult.AccessToken;

                        Console.WriteLine("\n\n");
                        Console.WriteLine($"access token:   {refreshResult.AccessToken}");
                        Console.WriteLine($"refresh token:  {refreshResult?.RefreshToken ?? "none"}");
                    }
                }
                if (key.Key == ConsoleKey.C)
                {
                    var logoutRequest = new LogoutRequest
                    {
                        IdTokenHint = result.IdentityToken,
                    };
                    var logoutResult = await _oidcClient.LogoutAsync(logoutRequest);
                    Console.WriteLine("\n\n");
                    Console.WriteLine($"Logged out");
                    return;
                }

                if (!response.IsSuccessStatusCode)
                {
                    await WriteError(response);
                    response = new HttpResponseMessage(); // Clear response
                }
            }
        }

        private static async Task<HttpResponseMessage> CallApi(string method, string currentAccessToken, string route, string payload = "")
        {
            _apiClient.DefaultRequestHeaders.Authorization =
                new AuthenticationHeaderValue("Bearer", currentAccessToken);
            if (method.ToUpper() == "GET")
            {
                return await _apiClient.GetAsync(route);
            }
            else if (method.ToUpper() == "POST")
            {
                var content = new StringContent(payload, Encoding.UTF8, "application/vnd.api+json");
                content.Headers.ContentType.CharSet = ""; // Important!
                return  await _apiClient.PostAsync(route, content);
            }
            throw new ArgumentException($"Method '{method}' not implemented");
        }

        private static Objekter CreateObjekt()
        {
            var temakode = new JsonApiSerializer.JsonApi.Relationship<Temakode>() { Data = new Temakode() { Id = "2140" } };  // 2140  fredede_omr_bk
            var reader = new WKTReader();
            var geometry = reader.Read("MULTIPOLYGON (((488884 6114493, 488984 6114493, 488984 6114393, 488884 6114393, 488884 6114493)))");
            geometry.SRID = 25832;

            var obj = new Objekter()
            {
                Temakode = temakode,
                OprindkodeId = 1, // Ortofoto
                StatuskodeId = 1, // Kladde
                OffKodeId = 1, // Synlig for alle
                Shape = geometry as MultiPolygon,
            };

            obj.Temaattributter = new Dictionary<string, object>
            {
                { "fred-tkode-id", 1 }, // Arealfredning
                { "aendr-kode-id", 4 }, // Generel ajourføring
                { "reg-nr", "1234" },
                { "gyldig-fra", "2020-08-19T12:34:56.789000+00:00" }
            };

            return obj;
        }

        private static void WriteTemakoder(IList<Temakode> temakoder)
        {
            Console.WriteLine("\n");
            Console.WriteLine($"#temakoder: {temakoder.Count}");
            var sortTemakoder = temakoder.OrderBy(tk => tk.Id);
            foreach (var temakode in sortTemakoder)
            {
                Console.WriteLine($"Id: {temakode.Id}  GeomType: {temakode.GeometryType.PadRight(20)} Name: {temakode.Name.PadRight(25)} Title: {temakode.Title}");
            }
        }

        private static void WriteAttributter(IList<Attribut> attributter, bool writeDomainValues = false)
        {
            Console.WriteLine("\n");
            Console.WriteLine($"#attributter: {attributter.Count}");
            var sortAttributter = attributter.OrderBy(a => a.Id);
            foreach (var attr in sortAttributter)
            {
                Console.WriteLine($"Id: {attr.Id.PadRight(25)}  Name: {attr.Name.PadRight(25)} Title: {attr.Title.PadRight(30)} DataType: {attr.DataType.PadRight(10)} Required: {attr.Required.ToString().PadRight(7)} Readonly: {attr.Readonly.ToString().PadRight(7)}");
                if (attr.DataType == "domain" && writeDomainValues) // loop domain values
                {
                    Console.WriteLine($"    Domain values for '{attr.Name}'");
                    foreach (var item in attr.Domain)
                    {
                        Console.WriteLine($"      {item.Key}: {item.Value}");
                    }
                }
            }
        }
        private static void WriteObjekter(IList<Objekter> objekter)
        {
            Console.WriteLine("\n");
            Console.WriteLine($"#objekter: {objekter.Count}");
            var sortObjekter = objekter.OrderBy(o => o.ObjektId).ThenBy(o => o.SystidFra);
            foreach (var obj in sortObjekter)
            {
                Console.WriteLine($"ObjektId: {obj.ObjektId}  VersionId: {obj.VersionId} Tema: {obj.Temakode.Data.Name.PadRight(20)} DataType: {obj.StatuskodeId}  SystidFra: {obj.SystidFra.ToString()}");
            }
        }


        private static async Task WriteError(HttpResponseMessage response)
        {
            var payload = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"\n\nStatusCode: {response.StatusCode}, Error: {response.ReasonPhrase}, Payload: {payload}");

        }

        #endregion
    }
}