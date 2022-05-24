using System.Collections;
using System.Text.Json;
using System.Collections.Generic;
using System.Drawing;

namespace MagicC;

public static class Locations
{
    public const string ResourceFolder = @"C:\Users\George Rahul\Desktop\Github\Elsa\resourcesnew\";
    public const string UserFile = @$"{ResourceFolder}users_hash.elsa";
    public const string ThemeFile = @$"{ResourceFolder} initial.elsa";
    
}

public class Json
{
    public Dictionary<string, string>? Dictionary(string fileUrl)
    {
        using FileStream fileRead = File.OpenRead(fileUrl);
        return JsonSerializer.Deserialize<Dictionary<string, string>>(fileRead);
    }

    public  List<string>? List(string fileUrl)
    {
        using FileStream fileRead = File.OpenRead(fileUrl);
        return JsonSerializer.Deserialize<List<string>>(fileRead);
    }

    public void Write<TJsonType>(string fileUrl,
            TJsonType jsonData) //Making the generic function to accept any kind of data
    {
        File.WriteAllText(fileUrl, JsonSerializer.Serialize(jsonData));
    }
    
}

public class Tools
{
    public IEnumerable Range(int stop,int start=0)
    {
        return Enumerable.Range(start,stop);
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
