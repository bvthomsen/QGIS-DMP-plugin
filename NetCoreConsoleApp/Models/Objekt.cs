using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using JsonApiSerializer.JsonApi;
using NetTopologySuite.Geometries;

namespace DAI.Edit.Models
{
    public class Objekter
    {
        public Guid Id { get; set; }
        [JsonProperty(propertyName: "objekt-id")]
        public Guid ObjektId { get; set; }
        [JsonProperty(propertyName: "version-id")]
        public Guid VersionId { get; set; }
        [JsonProperty(propertyName: "systid-fra")]
        public DateTimeOffset SystidFra { get; set; }
        [JsonProperty(propertyName: "systid-til")]
        public DateTimeOffset? SystidTil { get; set; }
        public DateTimeOffset Oprettet { get; set; }
        [JsonProperty(propertyName: "oprindkode-id")]
        public int OprindkodeId { get; set; }
        [JsonProperty(propertyName: "statuskode-id")]
        public int StatuskodeId { get; set; }
        [JsonProperty(propertyName: "off-kode-id")]
        public int OffKodeId { get; set; }
        [JsonProperty(propertyName: "cvr-kode-id")]
        public int CvrKodeId { get; set; }
        [JsonProperty(propertyName: "bruger-id")]
        public Guid? BrugerId { get; set; }
        public string Link { get; set; }
        public Geometry Shape { get; set; }
        public IDictionary<string, object> Temaattributter { get; set; }
        public Relationship<Temakode> Temakode { get; set; }
    }
}