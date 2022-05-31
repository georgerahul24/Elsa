using System.Collections;
using System.Runtime.CompilerServices;
using System.Text.Json;

namespace Magic;

public static class DataFileManager
{
    public const string ResourceFolder = @".\ResourceFolder\";
    public const string ResourceFile = @$"{ResourceFolder}data.elsa";

    private static Json _json = new(ResourceFile);
    //public const string UserFile = @$"{ResourceFolder}users_hash.elsa";
    //public const string ThemeFile = @$"{ResourceFolder} initial.elsa";
    public static int InitializeResourceFile()
    {

        try
        {
            Directory.CreateDirectory(ResourceFolder);
        }
        catch{}
        try
        {
            File.Delete(ResourceFile);
            
        }
        catch{}

        File.Create(ResourceFile).Close();



        Dictionary<string, Dictionary<string, string>> DataDictionary = new()
        {
            //Initializing Theme
            {
                "Theme", new Dictionary<string, string>
                {
                    { "fg", "#000000" },
                    { "bg", "#ffffff" },
                    { "bu", "#abcd12" }
                }
            },

            //Initialising Users
            {
                "Users", new Dictionary<string, string> { { "admin", "1234" } }
            }
        };
        
        _json.Write(DataDictionary);
        return 1;
    }
    
    public static Dictionary<string,string> Read(string name)
    {
        return _json.DictionaryResourceFile()?[name];
        
    }
    
    public static int Write(string filename, Dictionary<string, string> data)
    {
        Dictionary<string, Dictionary<string, string>> resourceData = _json.DictionaryResourceFile();
        try
        {
            
            resourceData[filename] = data;
            _json.Write(resourceData); //TODO:Check if the jsonType is inferred automatically
            return 1;
                
        }

        catch (Exception e)
        {
            Console.WriteLine(e);
            return -1;
        }

    }
}





public class Json
{
    private readonly string _fileUrl;

    public Json(string fileUrl)
    {
        this._fileUrl = fileUrl;
    }
        public Dictionary<string, Dictionary<string, string>>? DictionaryResourceFile()
        {
            using FileStream fileRead = File.OpenRead(_fileUrl);
            return JsonSerializer.Deserialize<Dictionary<string, Dictionary<string,string>>>(fileRead);
        }
        
        public Dictionary<string, string>? Dictionary()
        {
            using FileStream fileRead = File.OpenRead(_fileUrl);
            return JsonSerializer.Deserialize<Dictionary<string, string>>(fileRead);
        }

        public List<string>? List()
        {
            using FileStream fileRead = File.OpenRead(_fileUrl);
            return JsonSerializer.Deserialize<List<string>>(fileRead);
        }

        public void Write<TJsonType>(TJsonType jsonData) //Making the generic function to accept any kind of data
        {
            File.WriteAllText(_fileUrl, JsonSerializer.Serialize(jsonData));
        }

    }

    public class Tools
    {
        public IEnumerable Range(int stop, int start = 0)
        {
            return Enumerable.Range(start, stop);
        }

        public void Print<T>(T text)
        {
            Console.WriteLine(text);
        }

        string? Input(string inpText)
        {
            Console.Write(inpText);
            return Console.ReadLine();
        }
    }

