using System;
using System.Drawing;
using System.Windows.Forms;

namespace GUITest2
{
    public partial class Form1 : Form
    {
        Color background_leave = Color.FromArgb(30, 0, 61);
        Color background_enter = Color.FromArgb(52, 0, 93);
        Color forecolor_enter = Color.HotPink;
        Color forecolor_leave = Color.FromArgb(155, 89, 182);

        public Form1()
        {
            InitializeComponent();


        }
        void Hover_Enter(Button button)
        {
            button.BackColor = this.background_enter;
            button.ForeColor = this.forecolor_enter;
            panel1.Left = button.Left;
        }
        void Hover_Leave(Button button)
        {
            button.BackColor = this.background_leave;
            button.ForeColor = this.forecolor_leave;
            ;
        }
        private void btnGeneral_Click(object sender, EventArgs e)
        {
            titleLabel.Text = "GENERAL";
            panelStage.Controls.Clear();
        }
        private void btnGeneral_MouseEnter(object sender, EventArgs e)
        {
            Hover_Enter(sender as Button);
        }
        private void btnGeneral_MouseLeave(object sender, EventArgs e)
        {
            Hover_Leave(sender as Button);
        }

        private void btnTheme_MouseEnter(object sender, EventArgs e)
        {
            Hover_Enter(sender as Button);
        }

        private void btnTheme_MouseLeave(object sender, EventArgs e)
        {
            Hover_Leave(sender as Button);
        }

        private void btnIndexer_Click(object sender, EventArgs e)
        {

        }

        private void btnIndexer_MouseEnter(object sender, EventArgs e)
        {
            Hover_Enter(sender as Button);
        }

        private void btnIndexer_MouseLeave(object sender, EventArgs e)
        {
            Hover_Leave(sender as Button);
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

        }

        private void btnAbout_MouseEnter(object sender, EventArgs e)
        {
            Hover_Enter(sender as Button);
        }

        private void btnAbout_MouseLeave(object sender, EventArgs e)
        {

            Hover_Leave(sender as Button);

        }



        private void titleTheme_Paint(object sender, PaintEventArgs e)
        {
            titleLabel.BackColor = Color.Transparent;
        }

        private void btnClose_Paint(object sender, PaintEventArgs e)
        {

        }

        private void btnClose_Click(object sender, EventArgs e)
        {

            this.Close();

        }
    }
}
