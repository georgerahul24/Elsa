namespace SearchBar
{   
    
    public static class ElsaBackend
    {
        private static  bool followupquestion = false;//know if the input should be evaluated as a followup question.
        private static string followupsection = "";
        private static Magic.History history = new("admin");
        
        public static void Process(string command)
        {
            
            string[] commandParts = command.Split(' ', 2);
            string keyword = commandParts[0].Trim().ToLower();
            //string[] s = { "hi" };
            
            if (followupquestion==true)
                switch (followupsection)
                {
                    case "greeting":
                        Magic.Speech.Speak(FollowUpManager.Greeting(command));
                        history.Write(command, $"Replied the follow-up greeting");
                        break;
                }

            followupquestion = false;    
                        
            
            //if followup is not true
            switch (keyword){
                case "hi" or "hello":
                    Magic.Speech.Speak($"{keyword}. How do you Do?");
                    history.Write(command, "Replied to the Greeting");
                    followupquestion = true;
                    followupsection = "greeting";
                    break;
                case "t":
                    SearchBarGUI.StartUp.Start();
                    history.Write(command, "Ran Maintaninence Checks of Elsa");
                    break;
                case "export":
                    Magic.DataFileManager.ExportData.Export();
                    history.Write(command, "Exported Data");
                    break;


                case "bye" or "tata" or "exit":
                    Magic.Speech.Speak("Bye Bye. See you soon later.");
                    history.Write(command, "Exited Elsa");
                    Application.Exit();
                    break;



            }




        }
    }

    public static class FollowUpManager
    {
        private static Dictionary<string,string> GreetingFollowUp = new Dictionary<string, string>()
        {
            {"i am fine","Oh! Thats great. Lets make it better." },
            {"i am not fine","That is sad to hear. Do not worry. Better times are to follow."}
                };
        public static string Greeting(string command)
        {
            try
            {
                return GreetingFollowUp[command];
            }
            catch (KeyNotFoundException)
            {
                return "";
            }
        }

    }
}
