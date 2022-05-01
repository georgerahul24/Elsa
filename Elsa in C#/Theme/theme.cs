using System.Diagnostics;
namespace Theme
{

   

    public class theme
    {

        static private string FileRead(string fileLocation)
        {

            return File.ReadAllLines(fileLocation).First();
        }
        public List<string> ThemeReader()
        {
            
            string themeString=FileRead(@"C:\Users\George Rahul\Desktop\GUI\Theme\ initial.elsa");

            List<string> themeData=themeString.Split(';').ToList();
            return themeData;

        }

    }
}


