using System.Collections.Generic;
using System.Text.Json;
namespace Magic;

public class Usernames
{
    private string fileURL = @"C:\Users\George Rahul\Desktop\Github\Elsa\Elsa in C#\Theme\usernames.elsa";

    private Dictionary<string, string>? jsonRead()
    {
        using FileStream file_read = File.OpenRead(fileURL);
        
        return JsonSerializer.Deserialize<Dictionary<string,string>>(file_read);
        
    }
    public int write(string username, string password)
    {
        try
        {
            Dictionary<string, string>? userDictionary = jsonRead();
            userDictionary.Add(username, password);
            File.WriteAllText(fileURL, JsonSerializer.Serialize(userDictionary));
            return 1;
        }
        catch (ArgumentException)
        {
            Dictionary<string, string>? userDictionary = jsonRead();
            userDictionary.Remove(username);
            userDictionary.Add(username,password);
            File.WriteAllText(fileURL, JsonSerializer.Serialize(userDictionary));
            return 1;

        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            return -1;
            
        }
    }

    public string? check(string username)
    {  // Returns password if the user exists
        Dictionary<string, string>? userDictionary = jsonRead();
        if (userDictionary.ContainsKey(username))
        {
            return userDictionary[username];
        }
        return null;
    }

}