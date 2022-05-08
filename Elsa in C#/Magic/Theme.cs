namespace Magic;

using System.Drawing;

public class Theme
{
    private static readonly string InitialFileUrl = Locations.ThemeFile;

    private static string FileRead(string fileLocation)
    {
        return File.ReadAllLines(fileLocation).First();
    }

    public List<Color> ThemeReader()
    {
        string themeString = FileRead(InitialFileUrl);

        string[] themeDataString = themeString.Split(';');
        List<Color> themeData = new List<Color>();
        foreach (var themeColorString in themeDataString)

        {
            themeData.Add(ColorTranslator.FromHtml(themeColorString));
        }

        return themeData;
    }
}