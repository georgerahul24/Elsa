using System.Diagnostics;

namespace Magic;

public class History

{
    private string _username;

    public History(string username)
    {
        this._username = username;
    }
    public void Write(string userInput,string output)
    { 
        //This file is to save the history to user file
        using StreamWriter w = File.AppendText(Locations.resourceFolder+_username+".ElsaHistory");
        w.WriteLine($"{DateTime.Now:F} : {userInput} : {output}");
    }

    public void Read()
    {
        Process.Start($"notepad.exe", $"{Locations.resourceFolder+_username+".ElsaHistory"}");
    }
    
}