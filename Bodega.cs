using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ppai
{
    public class Bodega
    {
        public string Nombre { get; set; }
        public string CoordenadasUbicacion { get; set; }
        public string Descripcion { get; set; }
        public string Historia { get; set; }
        public int PeriodoActualizacion { get; set; }
        public List<Vino> Vinos { get; set; }

        public Bodega()
        {
            Vinos = new List<Vino>(); // Inicializar la lista de vinos
        }
    }

}
