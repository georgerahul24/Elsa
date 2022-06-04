namespace SearchBar
{
    public partial class SearchBar : Form
    {
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
    }
}