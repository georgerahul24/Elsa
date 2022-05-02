using Magic;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
namespace GUITest2
{
    public partial class ThemePage : Form
    {
        private Theme theme = new Theme();

        Color fgColor { get; set; }
        Color bgColor { get; set; }
        Color txtColor { get; set; }

        public ThemePage()
        {
            
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
    }
}
