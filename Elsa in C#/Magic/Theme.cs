
namespace Magic;
using System.Drawing;

public static class Theme
{
   
   
    

    public static List<Color>? ThemeReader()
    {
        List<string>? colorStrings = new(DataFileManager.Read("Theme").Values);
        List<Color> colorList = new();
        foreach (string color in colorStrings!)
        {
         colorList.Add(ColorTranslator.FromHtml(color));   
        }

        return colorList;

    }
}