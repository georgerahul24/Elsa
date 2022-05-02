namespace Magic;


using System.Drawing;
public class Theme
    {
    private string initialFileUrl = @"C:\Users\George Rahul\Desktop\Github\Elsa\resources\ initial.elsa";
        static private string FileRead(string fileLocation)
        {

            return File.ReadAllLines(fileLocation).First();
        }
        public List<Color> ThemeReader()
        {
            
            string themeString=FileRead(initialFileUrl);

            string[]  themeDataString=themeString.Split(';');
            List<Color> themeData = new List<Color>();
            foreach (var themecolorstring in themeDataString)
                
            {
                themeData.Add(ColorTranslator.FromHtml(themecolorstring));
            }
            return themeData;

        }


    }



