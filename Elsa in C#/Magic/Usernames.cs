using System.Text.Json;
namespace Magic;

public class Usernames
{
    private string fileURL = @"C:\Users\George Rahul\Desktop\Github\Elsa\resources\ users.elsa";

    private Dictionary<string, string>? JsonRead()
    {
        using FileStream fileRead = File.OpenRead(fileURL);
        
        return JsonSerializer.Deserialize<Dictionary<string,string>>(fileRead);
        
    }
    public int Write(string username, string password)
    {
        try
        {
            Dictionary<string, string>? userDictionary = JsonRead();
            userDictionary?.Add(username, password);
            File.WriteAllText(fileURL, JsonSerializer.Serialize(userDictionary));
            return 1;
        }
        catch (ArgumentException)
        {
            Dictionary<string, string>? userDictionary = JsonRead();
            userDictionary?.Remove(username);//Removing and adding user again to update the password
            userDictionary?.Add(username,password);
            File.WriteAllText(fileURL, JsonSerializer.Serialize(userDictionary));
            return 1;

        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            return -1;
            
        }
    }

    public bool Check(string username,string password)
    {  // Returns password if the user exists
        Dictionary<string, string>? userDictionary = JsonRead();
        if (userDictionary != null && userDictionary.ContainsKey(username))
        {
            return userDictionary[username]==password;
        }
        return false;
    }

}