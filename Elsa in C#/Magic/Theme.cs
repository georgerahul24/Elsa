
namespace Magic;
using System.Drawing;

public class Theme
{
   
   
    

    public List<Color>? ThemeReader()
    {
        List<string>? colorStrings = new List<string>(DataFileManager.Read("Theme").Values);
        List<Color> colorList = new List<Color>();
        foreach (string color in colorStrings!)
        {
         colorList.Add(ColorTranslator.FromHtml(color));   
        }

        return colorList;

    }
}