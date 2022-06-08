namespace HistoryGUI
{



    public partial class HistoryPageGUI : Form
    {

        public HistoryPageGUI(string? username, string history)
        {

            this.Text = username;


            InitializeComponent();
            textBlockHistoryData.Text = history;
        }

        private void HistoryPageGUI_Load(object sender, EventArgs e)
        {

        }

        private void textBlockHistoryData_TextChanged(object sender, EventArgs e)
        {

        }
    }

    public static class HistoryDisplay
    {
       [STAThread]
        public static void Display(string? username, string history)
        {

            HistoryPageGUI hist = new(username,history);
            hist.Show();
        }
    }
}