using System;
using Newtonsoft.Json;

namespace DAI.Edit.Models
{
    public class Temakode
    {
        public string Id { get; set; }
        public string Title { get; set; }
        public string Name { get; set; }
        [JsonProperty(propertyName: "geometry-type")]
        public string GeometryType { get; set; }
    }
}

