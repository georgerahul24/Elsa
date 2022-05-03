using Magic;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
namespace GUITest2
{
    public partial class ThemePage : Form
    {
        Form1 form1 = new Form1(); //to pass the forecolor
        private Theme theme = new Theme();
     
        

        Color fgColor { get; set; }
        Color bgColor { get; set; }
        Color txtColor { get; set; }

        public ThemePage()
        {
            this.SetStyle(ControlStyles.SupportsTransparentBackColor, true);
            List<Color> colors = theme.ThemeReader();
            bgColor = colors[0]; fgColor = colors[1]; txtColor = colors[2];
            InitializeComponent();

        }

        private void ThemePage_Load(object sender, EventArgs e)
        {

        }

        private void btnBGPeview_Paint(object sender, PaintEventArgs e)
        {

            btnBGPeview.BackColor = bgColor;

        }

        private void btnBGPeview_Click(object sender, EventArgs e)
        {

        }

        private void btnTextPreview_Paint(object sender, PaintEventArgs e)
        {
            btnTextPreview.BackColor = txtColor;
        }

        private void btnFGPreview_Paint(object sender, PaintEventArgs e)
        {
            btnFGPreview.BackColor = fgColor;
        }

        private void ThemePage_Paint(object sender, PaintEventArgs e)
        {
            this.BackColor = Color.Transparent;
        }

        private void labelBgPreview_Paint(object sender, PaintEventArgs e)
        {
            
            labelBgPreview.ForeColor = form1.forecolorColor;
        }

        private void labelTextPreview_Paint(object sender, PaintEventArgs e)
        {
            
            labelTextPreview.ForeColor = form1.forecolorColor;
        }

        private void labelFgPreview_Paint(object sender, PaintEventArgs e)
        {
            
            labelFgPreview.ForeColor= form1.forecolorColor;
        }
    }
}
