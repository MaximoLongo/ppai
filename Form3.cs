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
    public partial class Form3 : Form
    {
        private List<Bodega> listaBodegas;
        private Bodega bodegaSeleccionada;
        public Vino vinoTemporal;


        public Form3(List<Bodega> bodegas)
        {
            InitializeComponent();
            listaBodegas = bodegas;
            textBox2.Text = DateTime.Now.ToString("yyyy-MM-dd");

            // Poblar el ComboBox con las bodegas disponibles
            comboBox1.DataSource = listaBodegas;
            comboBox1.DisplayMember = "Nombre"; // Establece la propiedad a mostrar en el ComboBox


        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            vinoTemporal = new Vino
            {
                Nombre = textBox4.Text,
                Añada = Convert.ToInt32(textBox1.Text),
                NotaDeCataBodega = textBox5.Text,
                PrecioARS = Convert.ToDecimal(textBox6.Text),
                FechaActualizacion = DateTime.Now
            };

            // Mostrar un mensaje de éxito
            MessageBox.Show("Vino guardado");
            bodegaSeleccionada = (Bodega)comboBox1.SelectedItem;

            // Cerrar la ventana
            this.Close();

            ActualizarBodega actualizarBodega = new ActualizarBodega(listaBodegas);

            // Mostrar el formulario de actualización de bodega
            actualizarBodega.Show();

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex >= 0)
            {
                // Obtiene la bodega seleccionada
                bodegaSeleccionada = (Bodega)comboBox1.SelectedItem;
            }
        }
        
    }
}
