using System.Security.Cryptography;
using System.Text;

namespace MagicC;

public class Usernames
{
    private readonly string _fileUrl = Locations.UserFile;
    private readonly Json _json = new Json();

    private string Hash(string text)
    {
        using SHA512 sha512Hash = SHA512.Create();
        byte[] bytes = sha512Hash.ComputeHash(Encoding.UTF32.GetBytes(text + "Elsa"));

        // Convert byte array to a string   
        StringBuilder builder = new StringBuilder();
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
            Dictionary<string, string>? userDictionary = _json.Dictionary(_fileUrl);
            if (userDictionary != null)
            {
                userDictionary[username] = password;
                _json.Write(_fileUrl, userDictionary); //TODO:Check if the jsonType is inferred automatically
                return 1;
            }

            return -1;

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
        Dictionary<string, string>? userDictionary = _json.Dictionary(_fileUrl);
        if (userDictionary != null && userDictionary.ContainsKey(username))
        {
            return userDictionary[username] == password;
        }

        return false;
    }
}