using System.Text.Json;

namespace Magic;

using System.Drawing;

public class Theme
{
    private static readonly string InitialFileUrl = Locations.ThemeFile;
    private Json _json = new Json();
    

    public List<Color>? ThemeReader()
    {
        List<string>? colorStrings = _json.List(InitialFileUrl);
        List<Color> colorList = new List<Color>();
        foreach (string color in colorStrings)
        {
         colorList.Add(ColorTranslator.FromHtml(color));   
        }

        return colorList;

    }
}