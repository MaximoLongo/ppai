using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ppai
{
    public partial class Form1 : Form
    {
        private List<Bodega> listaBodegas;

        public Form1()
        {
            InitializeComponent();
            InicializarListaBodegas();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ActualizarBodega actualizarBodega = new ActualizarBodega(listaBodegas);

            // Mostrar el formulario de actualización de bodega
            actualizarBodega.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click_1(object sender, EventArgs e)
        {

        }

        private void button3_Click_1(object sender, EventArgs e)
        {

        }

        private void InicializarListaBodegas()
        {
            // Inicializar la lista de bodegas
            listaBodegas = new List<Bodega>();

            // Agregar algunas bodegas de ejemplo con vinos
            var bodegaA = new Bodega
            {
                Nombre = "Bodega A",
                CoordenadasUbicacion = "123,456",
                Descripcion = "Descripción de la Bodega A",
                Historia = "Historia de la Bodega A",
                PeriodoActualizacion = 2 // Por ejemplo, actualización cada 2 meses
            };
            bodegaA.Vinos.Add(new Vino
            {
                Nombre = "Vino 1",
                Añada = 2019,
                FechaActualizacion = DateTime.Now,
                NotaDeCataBodega = "Nota de cata para Vino 1",
                PrecioARS = 100
            });
            bodegaA.Vinos.Add(new Vino
            {
                Nombre = "Vino 2",
                Añada = 2020,
                FechaActualizacion = DateTime.Now,
                NotaDeCataBodega = "Nota de cata para Vino 2",
                PrecioARS = 120
            });

            listaBodegas.Add(bodegaA);

            var bodegaB = new Bodega
            {
                Nombre = "Bodega B",
                CoordenadasUbicacion = "789,012",
                Descripcion = "Descripción de la Bodega B",
                Historia = "Historia de la Bodega B",
                PeriodoActualizacion = 3 // Por ejemplo, actualización cada 3 meses
            };
            bodegaB.Vinos.Add(new Vino
            {
                Nombre = "Vino 3",
                Añada = 2018,
                FechaActualizacion = DateTime.Now,
                NotaDeCataBodega = "Nota de cata para Vino 3",
                PrecioARS = 90
            });
            bodegaB.Vinos.Add(new Vino
            {
                Nombre = "Vino 4",
                Añada = 2021,
                FechaActualizacion = DateTime.Now,
                NotaDeCataBodega = "Nota de cata para Vino 4",
                PrecioARS = 110
            });

            listaBodegas.Add(bodegaB);

            // Agregar más bodegas con sus respectivos vinos según sea necesario
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            Form3 agregarVinoForm = new Form3(listaBodegas);
            agregarVinoForm.ShowDialog();

           
        }
    }
}
