namespace MagicC;

public class Data
{
    public static void Export()
    {
        Json json = new();
        Dictionary<string, string>? userdata = json.Dictionary(Locations.UserFile);
        
    }
}