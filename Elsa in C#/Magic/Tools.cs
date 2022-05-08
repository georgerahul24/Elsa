using System.Collections;
using System.Text.Json;
using System.Collections.Generic;
namespace Magic;

public static class Locations
{
    public const string UserFile = @"C:\Users\George Rahul\Desktop\Github\Elsa\resourcesnew\users_hash.elsa";
    public const string ThemeFile = @"C:\Users\George Rahul\Desktop\Github\Elsa\resourcesnew\ initial.elsa";
    public const string resourceFolder = @"C:\Users\George Rahul\Desktop\Github\Elsa\resourcesnew\";
}

public class Json
{
    public Dictionary<string, string> Read(string fileUrl)
    {
        using FileStream fileRead = File.OpenRead(fileUrl);
        return JsonSerializer.Deserialize<Dictionary<string, string>>(fileRead);
    }

    public static List<string> ReadList(string fileUrl)
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
