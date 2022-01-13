using System;
using JsonApiSerializer.JsonApi;

namespace DAI.Edit.Models
{
    public class Temaattribut : Attribut
    {
        public Relationship<Temakode> Temakode { get; set; }
    }
}