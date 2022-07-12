namespace SearchBar
{
    public partial class SearchBar : Form
    {
        private static readonly Dictionary<string, Color> colors = Magic.Theme.ThemeReader("admin");
        public SearchBar()
        {
            InitializeComponent();

        }

        /*
        protected override void OnDeactivate(EventArgs e)
        {
           Application.Exit();//Close the application if it loses the focus.
        }*/
        private void SearchBoxButton_Click(object sender, EventArgs e)
        {
            //MessageBox.Show(SearchBoxTextInput.Text);
            SearchBoxButton.Focus();//To make sure that the focus has been moved away from the text box..when pressing the enter key also..
            ElsaBackend.Process(SearchBoxTextInput.Text);
            SearchBoxTextInput.Text = "Search....";


        }

        private void SearchBoxTextInput_Enter(object sender, EventArgs e)
        {
            SearchBoxTextInput.Text = "";
        }



        private void SearchBar_KeyDown(object sender, KeyEventArgs e)
        {

            if (e.KeyCode == Keys.Escape)//Close the application if the 'Esc' key is pressed.
            {
                Application.Exit();
            }
        }

        private void SearchBoxButton_Paint(object sender, PaintEventArgs e)
        {
            SearchBoxButton.ForeColor = colors["ButtonColor"];
            SearchBoxTextInput.ForeColor = colors["ForeColor"];
            SearchBoxTextInput.BackColor = colors["BackColor"];
        }

        private void SearchBoxTextInput_TextChanged(object sender, EventArgs e)
        {
            Magic.Autocomplete.Clear();
            //SearchBoxTextInput.AutoCompleteCustomSource = Magic.Autocomplete.Suggestions();
            
            
            
        }
    }
}