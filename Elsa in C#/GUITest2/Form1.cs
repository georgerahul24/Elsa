using System;
using System.Drawing;
using System.Windows.Forms;

namespace GUITest2
{
    public partial class Form1 : Form
    {
        public Color backgroundColor = ColorTranslator.FromHtml("#1f1f1f");
        public Color forecolorColor = ColorTranslator.FromHtml("#d4d4d4");
        Color stageBG = ColorTranslator.FromHtml("#888888");
        //Color backgroundColor = Color.FromArgb(30, 0, 61);
        //Color forecolorColor = Color.FromArgb(155, 89, 182);
     

        public Form1()
        {
            InitializeComponent();


        }
        

     
        private void btnGeneral_Click(object sender, EventArgs e)
        {
            titleLabel.Text = "GENERAL";
            panelStage.Controls.Clear();
           
        }
       
        private void btnTheme_Click(object sender, EventArgs e)
        {
            titleLabel.Text = "THEME";
            ThemePage themePage = new ThemePage() { Dock = DockStyle.Fill, TopLevel = false, TopMost = true };
            this.panelStage.Controls.Clear();
            this.panelStage.Controls.Add(themePage);
            themePage.Show();

        }

        private void btnAbout_Click(object sender, EventArgs e)
        {
            titleLabel.Text = "ABOUT";
            AboutPage about= new AboutPage() { Dock = DockStyle.Fill, TopLevel = false, TopMost = true };
            this.panelStage.Controls.Clear();
            this.panelStage.Controls.Add(about);
            about.Show();
        }

       
        private void btnClose_Click(object sender, EventArgs e)
        {

            this.Close();

        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {
            panel2.BackColor = backgroundColor;
        }

        private void btnGeneral_Paint(object sender, PaintEventArgs e)
        {
            btnGeneral.BackColor = backgroundColor;
            btnGeneral.ForeColor = forecolorColor;
        }

        private void btnTheme_Paint(object sender, PaintEventArgs e)
        {
            btnTheme.BackColor = backgroundColor;
            btnTheme.ForeColor = forecolorColor;
        }

        private void btnIndexer_Paint(object sender, PaintEventArgs e)
        {
            btnIndexer.BackColor = backgroundColor;   
            btnIndexer.ForeColor = forecolorColor;
        }

        private void btnAbout_Paint(object sender, PaintEventArgs e)
        {
            btnAbout.BackColor = backgroundColor;
            btnAbout.ForeColor = forecolorColor;
        }

        private void labelUserName_Paint(object sender, PaintEventArgs e)
        {
            labelUserName.BackColor = backgroundColor;
            labelUserName.ForeColor = forecolorColor;
        }

        private void navPanel1_Paint(object sender, PaintEventArgs e) => navPanel1.BackColor = backgroundColor;
      

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            this.BackColor = stageBG;
        }


        private void titleLabel_Paint(object sender, PaintEventArgs e)
        {
            titleLabel.ForeColor = forecolorColor;
        }

        private void btnClose_Paint(object sender, PaintEventArgs e)
        {
            btnClose.BackColor = backgroundColor;
            btnClose.ForeColor = forecolorColor;
        }

        private void titleLabel_Click(object sender, EventArgs e)
        {

        }
    }
}
