
namespace Magic;
using System.Drawing;

public static class Theme
{
    
   
    

    public static Dictionary<string,Color> ThemeReader(string username)
    {
        DataFileManager dataFileManager = new(username);
        List<Color> colorList = new();
        
        

        return dataFileManager.GetTheme();

    }
}