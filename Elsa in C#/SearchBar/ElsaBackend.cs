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
                    MagicC.Speech.Speak($"{keyword}. How do you Do?");
                    break;
                case "bye" or "tata" or "exit":
                    MagicC.Speech.Speak("Bye Bye See you soon later.");
                    Application.Exit();
                    break;

            }




        }
    }
}
