namespace Magic;

public class Data
{
    public void Export()
    {
        Json json = new Json();
        Dictionary<string, string>? userdata = json.Dictionary(Locations.UserFile);
        
    }
}