using System;
using System.IO;
using System.IO.Pipes;
using IdentityModel.OidcClient;
using System.Text.Json;
using System.Text;

namespace DMPLoginApp
{
    public class Program
    {
        static string _pname = "qgisplugin-integration-pipename";
        static string _clientId = "qgisplugin-integration-daiedittest";
        static string _host = "http://localhost";
        static int _port = 5001;
        static string _redirectUri = $"{_host}:{_port}/login";
        static string _postLogoutRedirectUri = $"{_host}:{_port}/login";
        static string _authority = "https://log-in.test.miljoeportal.dk/runtime/oauth2";
        static string _scope = "openid http://www.miljoeportal.dk/roles";
        static string _api = "https://arealeditering-api.udv.miljoeportal.dk/";

        static OidcClient _oidcClient;
        static string currentRefreshToken = "";
        static string currentIdentityToken = "";
        static int bufSize = 4096;

        public static int Main(string[] args)
        {
            Console.WriteLine("Program started");
            if (args.Length > 0)
            {
                // Get Named Pipe Server name from command line 
                _pname = args[0];
                Console.WriteLine("Pipe name = " + _pname);

                if (args.Length > 1)
                {
                    _clientId = args[1];
                    Console.WriteLine("Client Id = " + _clientId);

                    _host = args[2];
                    Console.WriteLine("Host = " + _host);

                    _port = Int32.Parse(args[3]);
                    Console.WriteLine("Port = " + args[3]);

                    _redirectUri = args[4];
                    Console.WriteLine("Redirect URL = " + _redirectUri);

                    _postLogoutRedirectUri = args[5];
                    Console.WriteLine("Logout Redirect URL = " + _postLogoutRedirectUri);

                    _authority = args[6];
                    Console.WriteLine("Authority = " + _authority);

                    _scope = args[7];
                    Console.WriteLine("Scope = " + _scope);

                    _api = args[8];
                    Console.WriteLine("Api = " + _api);
                }
            }

//            var PipeSecurity = new PipeSecurity();
//            var networkSid = new SecurityIdentifier(WellKnownSidType.NetworkSid, null);
//            PipeSecurity.AddAccessRule(new PipeAccessRule(networkSid, PipeAccessRights.FullControl, AccessControlType.Deny));

            // Named Pipe Server 
            var server = new NamedPipeServerStream(_pname, PipeDirection.InOut, 1, PipeTransmissionMode.Message);
            Console.WriteLine("Pipe started, Wait for connection");
            DMPrecord dmprec = new DMPrecord();

            server.WaitForConnection();
            Console.WriteLine("Connected...");
            bool anotherround = true;
            while (anotherround)
            {
                try
                {
                    StringBuilder messageBuilder = new StringBuilder();
                    string messageChunk = string.Empty;
                    do
                    {
                        byte[] messageBuffer = new byte[10];
                        server.Read(messageBuffer, 0, messageBuffer.Length);
                        messageChunk = Encoding.UTF8.GetString(messageBuffer);
                        messageBuilder.Append(messageChunk);
                    }
                    while (!server.IsMessageComplete);
 
                    var line = messageBuilder.ToString().Trim('\0');

                    dmprec.command = line;
                    dmprec.error = "";
                    dmprec.token = "";
                    dmprec.time = "";

                    Console.WriteLine("Command is: " + dmprec.command);


                    if (line == "login")
                    {
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

                        _oidcClient = new OidcClient(options);
                        var result = _oidcClient.LoginAsync(new LoginRequest()).GetAwaiter().GetResult();
                        if (result.IsError)
                        {
                            dmprec.error = result.Error;
                        }
                        else
                        {
                            currentRefreshToken = result.RefreshToken;
                            currentIdentityToken = result.IdentityToken;
                            dmprec.token = result.AccessToken;
                            dmprec.time = result.AccessTokenExpiration.ToString("s");
                        }
                        WriteDMPrecord(server, dmprec, bufSize);
                    }

                    else if (line == "refresh")
                    {
                        var result = _oidcClient.RefreshTokenAsync(currentRefreshToken).GetAwaiter().GetResult();
                        if (result.IsError)
                        {
                            dmprec.error = result.Error;
                        }
                        else
                        {
                            currentRefreshToken = result.RefreshToken;
                            currentIdentityToken = result.IdentityToken;
                            dmprec.token = result.AccessToken;
                            dmprec.time = result.AccessTokenExpiration.ToString("s");
                        }
                        WriteDMPrecord(server, dmprec, bufSize);
                    }

                    else if (line == "logout")
                    {
                        var logoutRequest = new LogoutRequest()
                        {
                            IdTokenHint = currentIdentityToken
                        };
                        var result = _oidcClient.LogoutAsync(logoutRequest).GetAwaiter().GetResult();
                        if (result.IsError)
                        {
                            dmprec.error = result.Error;
                        }
                        WriteDMPrecord(server, dmprec, bufSize);
                    }

                    else if (line == "stop")
                    {
                        Console.WriteLine("stop commando...");
                        WriteDMPrecord(server, dmprec, bufSize);
                        anotherround = false;
                    }
                    else
                    {
                        dmprec.error = "Unknown command : " + line;
                        WriteDMPrecord(server, dmprec, bufSize);
                    }
                }
                catch (EndOfStreamException)
                {
                    Console.WriteLine("EndOfStreamException");
                    anotherround = false;
                }
                catch (IOException)
                {
                    Console.WriteLine("IOException");
                    anotherround = false;
                }
            }

            server.Close();
            server.Dispose();

            return 0;
        }

        private static void WriteDMPrecord (NamedPipeServerStream server, DMPrecord dmprec, int bufsize)
        {
            var json = JsonSerializer.Serialize(dmprec);
            byte[] messageBytes = Encoding.UTF8.GetBytes(json);
            server.Write(messageBytes, 0, messageBytes.Length);
        }

        public class DMPrecord
        {
            public string command { get; set; }
            public string token { get; set; }
            public string time { get; set; }
            public string error { get; set; }
        }
    }
}