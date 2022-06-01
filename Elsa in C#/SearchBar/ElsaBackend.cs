namespace SearchBar
{   
    public static class ElsaBackend
    {
       
        public static void Process(string command)
        {
            string[] commandParts = command.Split(' ', 2);
            string keyword = commandParts[0].Trim().ToLower();
            //string[] s = { "hi" };
            switch (keyword){
                case "hi" or "hello":
                    Magic.Speech.Speak($"{keyword}. How do you Do?");
                    break;
                case "t":
                    SearchBarGUI.StartUp.Start();                 
                    break;
                case "bye" or "tata" or "exit":
                    Magic.Speech.Speak("Bye Bye. See you soon later.");
                    Application.Exit();
                    break;


            }




        }
    }
}
