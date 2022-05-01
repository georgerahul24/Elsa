
using System.Drawing;

namespace Theme
{

   

    public class theme
    {

        static private string FileRead(string fileLocation)
        {

            return File.ReadAllLines(fileLocation).First();
        }
        public List<Color> ThemeReader()
        {
            
            string themeString=FileRead(@"D:\Github\Elsa\Elsa in C#\Theme\ initial.elsa");

            string[]  themeDataString=themeString.Split(';');
            List<Color> themeData = new List<Color>();
            foreach (var themecolorstring in themeDataString)
                
            {
                themeData.Add(ColorTranslator.FromHtml(themecolorstring));
            }
            return themeData;

        }

    }
}


