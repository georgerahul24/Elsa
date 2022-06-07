using System.Diagnostics;
using System.IO;

namespace Magic;

public struct DataStruct
{
    public string? Password;
    public Dictionary<string, string> Theme;
    public List<string> History;

    public DataStruct()
    {
        Password = null;
        History = new List<string>();
        Theme = new Dictionary<string, string>()
        {
            { "fg", "#000000" },
            { "bg", "ffffff" },
            {"ButtonColor","#abc123"}
        };
    }
}

public class DataFileManager
{
    private static string _username;
    private const string ResourceFolder = @".\";
    private const string ResourceFile = @$"{ResourceFolder}data.ElsaData";
    private readonly Json _json;
    private DataStruct _userData;

    public DataFileManager(string username)
    {
        _username = username;
        _json = new(ResourceFile);
        try
        {
            _userData = _json.Read<Dictionary<string, DataStruct>>()[_username];
        }
        catch (KeyNotFoundException e)
        {
            Debug.WriteLine(e);
            _userData = new DataStruct();//just give the default values;
        }
    }


    public void InitializeResourceFile()
    {
        
        
            File.Create(ResourceFile).Close();
            //File.Delete(ResourceFile);
        
        Dictionary<string, DataStruct> dataDictionary = new();
        _userData.Password = new Usernames().Hash("1234");
        dataDictionary.Add("admin", _userData);
        _json.Write(dataDictionary);
    }


    public Dictionary<string, DataStruct>? DataDictionary()
    {
        return _json.Read<Dictionary<string, DataStruct>>();
    }


    public List<string> GetHistory()
    {
        return _userData.History;
    }

    public string GetPassword()
    {
        return _userData.Password;
    }

    public Dictionary<string, string> GetTheme()
    {
        return _userData.Theme;
    }

    public int Write(string dataName, object data)
    {
        switch (dataName)
        {
            case "History":
                _userData.History.Add((string)data);
                break;
            case "Password":
                _userData.Password = (string)data;
                break;
        }

        Dictionary<string, DataStruct>? dataDict = DataDictionary();
        dataDict[_username] = _userData;
        _json.Write(dataDict);
        return 1;
    }
}