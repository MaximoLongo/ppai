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
    public partial class ActualizarBodega : Form
    {
        private List<Bodega> listaBodegas;
        public Vino vinoTemporal;

        public ActualizarBodega(List<Bodega> bodegas)
        {
            InitializeComponent();
            listaBodegas = bodegas;



            // Asigna la lista de bodegas al ListBox
            listBoxBodegas.DataSource = listaBodegas;
            listBoxBodegas.DisplayMember = "Nombre"; // Establece la propiedad a mostrar en el ListBox
        }
        
        private void InitializeComponent()
        {
            this.label2 = new System.Windows.Forms.Label();
            this.listBoxBodegas = new System.Windows.Forms.ListBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.textBox5 = new System.Windows.Forms.TextBox();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.White;
            this.label2.Location = new System.Drawing.Point(231, 52);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(345, 73);
            this.label2.TabIndex = 0;
            this.label2.Text = "BON VINO";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // listBoxBodegas
            // 
            this.listBoxBodegas.BackColor = System.Drawing.Color.Black;
            this.listBoxBodegas.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listBoxBodegas.ForeColor = System.Drawing.Color.White;
            this.listBoxBodegas.FormattingEnabled = true;
            this.listBoxBodegas.ItemHeight = 25;
            this.listBoxBodegas.Location = new System.Drawing.Point(76, 160);
            this.listBoxBodegas.Name = "listBoxBodegas";
            this.listBoxBodegas.Size = new System.Drawing.Size(182, 254);
            this.listBoxBodegas.TabIndex = 1;
            this.listBoxBodegas.SelectedIndexChanged += new System.EventHandler(this.listBox1Bodegas_SelectedIndexChanged);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(510, 150);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 20);
            this.textBox1.TabIndex = 2;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(333, 193);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 20);
            this.textBox2.TabIndex = 3;
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(571, 193);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(100, 20);
            this.textBox3.TabIndex = 4;
            // 
            // textBox4
            // 
            this.textBox4.Location = new System.Drawing.Point(450, 193);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(100, 20);
            this.textBox4.TabIndex = 5;
            // 
            // textBox5
            // 
            this.textBox5.Location = new System.Drawing.Point(688, 193);
            this.textBox5.Name = "textBox5";
            this.textBox5.Size = new System.Drawing.Size(100, 20);
            this.textBox5.TabIndex = 6;
            // 
            // dataGridView1
            // 
            this.dataGridView1.BackgroundColor = System.Drawing.Color.White;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(333, 229);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(455, 150);
            this.dataGridView1.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.ForeColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point(507, 134);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 13);
            this.label1.TabIndex = 8;
            this.label1.Text = "NOMBRE";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.Color.White;
            this.label3.Location = new System.Drawing.Point(330, 177);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(90, 13);
            this.label3.TabIndex = 9;
            this.label3.Text = "COORDENADAS";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.ForeColor = System.Drawing.Color.White;
            this.label4.Location = new System.Drawing.Point(447, 177);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(87, 13);
            this.label4.TabIndex = 10;
            this.label4.Text = "DESCRIPPCION";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.ForeColor = System.Drawing.Color.White;
            this.label5.Location = new System.Drawing.Point(568, 177);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(58, 13);
            this.label5.TabIndex = 11;
            this.label5.Text = "HISTORIA";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.ForeColor = System.Drawing.Color.White;
            this.label6.Location = new System.Drawing.Point(685, 177);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(80, 13);
            this.label6.TabIndex = 12;
            this.label6.Text = "PERIODO ACT";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(510, 390);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 13;
            this.button1.Text = "ACTUALIZAR";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // ActualizarBodega
            // 
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(0)))), ((int)(((byte)(64)))));
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.textBox5);
            this.Controls.Add(this.textBox4);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.listBoxBodegas);
            this.Controls.Add(this.label2);
            this.Name = "ActualizarBodega";
            this.Load += new System.EventHandler(this.ActualizarBodega_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void listBox1Bodegas_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBoxBodegas.SelectedIndex >= 0)
            {
                // Obtiene la bodega seleccionada
                Bodega bodegaSeleccionada = (Bodega)listBoxBodegas.SelectedItem;

                // Muestra los detalles de la bodega seleccionada en los TextBox
                textBox1.Text = bodegaSeleccionada.Nombre;
                textBox2.Text = bodegaSeleccionada.CoordenadasUbicacion;
                textBox3.Text = bodegaSeleccionada.Descripcion;
                textBox4.Text = bodegaSeleccionada.Historia;
                textBox5.Text = bodegaSeleccionada.PeriodoActualizacion.ToString();

                // Muestra los vinos de la bodega seleccionada en el DataGridView
                dataGridView1.DataSource = bodegaSeleccionada.Vinos;
            }
        }

        private void ActualizarBodega_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listBoxBodegas.SelectedIndex >= 0 && vinoTemporal != null)
            {
                // Obtener la bodega seleccionada
                Bodega bodegaSeleccionada = (Bodega)listBoxBodegas.SelectedItem;

                // Agregar el vino temporal a la bodega seleccionada
                bodegaSeleccionada.Vinos.Add(vinoTemporal);

                // Mostrar un mensaje de éxito
                MessageBox.Show("Vino guardado en la bodega seleccionada.");

                // Reiniciar la variable temporal para el próximo vino
                vinoTemporal = null;
            }
            else
            {
                MessageBox.Show("Seleccione una bodega y complete los detalles del vino antes de guardarlo.");
            }
        }
    }
}
