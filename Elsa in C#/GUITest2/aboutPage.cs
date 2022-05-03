using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using GUITest2;
namespace GUITest2
{
    public partial class AboutPage : Form
    {
        Form1 form1 = new Form1();//to pass the forecolor
        
        public AboutPage()

        {
            this.SetStyle(ControlStyles.SupportsTransparentBackColor, true);
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void AboutPage_Paint(object sender, PaintEventArgs e)
        {
            this.BackColor = Color.Transparent;
        }

        private void createdbyLabel_Paint(object sender, PaintEventArgs e)
        {
            createdbyLabel.ForeColor = form1.forecolorColor;
        }

        private void versionLabel_Paint(object sender, PaintEventArgs e)
        {
            versionLabel.ForeColor= form1.forecolorColor;
        }
    }
}
