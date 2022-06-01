using System.Security.Cryptography;
using System.Text;

namespace Magic;

public class Usernames
{
    private readonly Dictionary<string,string>  UserData= DataFileManager.Read("Users");
   

    private static string Hash(string text)
    {
        using SHA512 sha512Hash = SHA512.Create();
        byte[] bytes = sha512Hash.ComputeHash(Encoding.UTF32.GetBytes(text + "Elsa"));

        // Convert byte array to a string   
        StringBuilder builder = new();
        foreach (var t in bytes)
        {
            builder.Append(t.ToString("x2"));
        }

        return builder.ToString();
    }

    public int Write(string username, string password)
    {
        password = Hash(password);
        try
        {
            
                UserData[username] = password;
                return DataFileManager.Write("Users",UserData); //TODO:Check if the jsonType is inferred automatically
               
                
        }

        catch (Exception e)
        {
            Console.WriteLine(e);
            return -1;
        }
    }

    public bool Check(string username, string password)
    {
        // Returns password if the user exists
        password = Hash(password);
        
        if (UserData.ContainsKey(username))
        {
            return UserData[username] == password;
        }
        return false;
    }
}