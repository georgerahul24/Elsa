
namespace Magic;
using System.Drawing;

public static class Theme
{
   
   
    

    public static List<Color> ThemeReader(string username)
    {
        DataFileManager dataFileManager = new(username);
        List<Color> colorList = new();
        foreach (string color in dataFileManager.GetTheme().Values)
        {
         colorList.Add(ColorTranslator.FromHtml(color));   
        }

        return colorList;

    }
}