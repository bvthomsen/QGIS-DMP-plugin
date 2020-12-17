using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace DAI.Edit.Models
{
    public class Attribut
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Title { get; set; }
        public bool Required { get; set; }
        public bool Readonly { get; set; }
        public string Default { get; set; }
        [JsonProperty(propertyName: "data-type")]
        public string DataType { get; set; }
        public IDictionary<string, string> Domain { get; set; }

        public string GetDomainValue(string key)
        {
            Domain.TryGetValue(key, out string value);
            return value;
        }
    }
}