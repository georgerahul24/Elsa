using System.Diagnostics;
using System.Drawing;
using System.IO;

namespace Magic;

public struct DataStruct
{
    public string? Password;
    public Dictionary<string, Color> Theme;
    public List<string> History;

    public DataStruct()
    {
        Password = null;
        History = new List<string>();
        Theme = new Dictionary<string, Color>
        {
            { "BackColor", ColorTranslator.FromHtml("#000000") },
            { "ForeColor", ColorTranslator.FromHtml("#ffffff") },
            {"ButtonColor",ColorTranslator.FromHtml("#abc123")}
        };
    }
}

public class DataFileManager
{
    private static string? _username;
    private const string ResourceFolder = @".\";//The folder location of the userdata
    public const string ResourceFile = @$"{ResourceFolder}data.ElsaData";
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
            _userData = new(); //just to give the default values incase the user is not found;
        }
        catch (FileNotFoundException)
        {
            InitializeResourceFile();

        }
    }


    public void InitializeResourceFile()
    {


        File.Create(ResourceFile).Close();
        //File.Delete(ResourceFile);

        Dictionary<string, DataStruct> dataDictionary = new();
        _userData = new();
        _userData.Password = Usernames.Hash("1234");
        dataDictionary.Add("admin", _userData);//Adding user Admin to the resource file.
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

    public Dictionary<string, Color> GetTheme()
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

    public static class ExportData{

        public static void  Export()
        {
            try
            {

                Speech.Speak("Hey! Choose a folder to where i should save the Data");
                File.WriteAllText(FolderChooser.Choose() + @"\Elsa.ElsaData", File.ReadAllText(DataFileManager.ResourceFile));
                Debug.Write("Data Exported Successfully");
                Speech.Speak("Thank You for waiting!Finished Exporting your data");
                
            }
            catch (System.UnauthorizedAccessException)
            {
                Speech.Speak("Hey! It seems that I do not have the necessary permissions to do this task.");
                Debug.Write("Could Not Complete Exporting data since permission to wrote to file was denied");
                
            }
            
        ; 
        }
         

        }


}