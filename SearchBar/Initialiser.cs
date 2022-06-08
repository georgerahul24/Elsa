
using Magic;
using Microsoft.VisualBasic.ApplicationServices;


namespace SearchBarGUI
{
    public static class StartUp
    {
        public static void Start()
        {
            Speech.Speak("Hello. I am just running some basic tests for you!");
            bool a = Usernames.Check("admin", "1234");
            bool b = Usernames.Check("admin", "123");
            bool c = Usernames.Check("test", "abcd");
            Usernames.Write("admin", "123");
            Usernames.Write("Test", "123");
            bool d = Usernames.Check("admin", "123");
            bool e = Usernames.Check("Test", "123");
            MessageBox.Show(@$"
Username admin tests:
 Correct passwd : {a},{d}
Incorrect Password: {b},{c}

Username Test
Before adding {c}
After adding {e}");
            
            
            History history = new History("admin");
            history.Write($"{DateTime.Now}", $"{DateTime.Now}");
            history.Read();


        }
    }
}
