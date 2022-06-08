﻿using System.Security.Cryptography;
using System.Text;

namespace Magic;

public static class Usernames
{
    //private readonly Dictionary<string,object>  UserData= DataFileManager.Data();
   

    public static string Hash(string text)
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

    public static int Write(string username, string password)
    {
        password = Hash(password);
        try
        {
            
                return new DataFileManager(username).Write("Password",password); //TODO:Check if the jsonType is inferred automatically
                


        }

        catch (Exception e)
        {
            Console.WriteLine(e);
            return -1;
        }
    }

    public static bool Check(string username, string password)
    {
        // Returns password if the user exists
        password = Hash(password);
        DataFileManager dataFileManager = new DataFileManager(username);


        return dataFileManager.GetPassword() == password;
    }
}