using HistoryGUI;
using System.IO;

namespace Magic;

public class History

{
    private readonly string _username;

    public History(string username)
    {
        _username = username;
    }
    public void Write(string userInput,string output)
    { 
        //This file is to save the history to user file
        using StreamWriter w = File.AppendText(DataFileManager.ResourceFolder+_username+".ElsaHistory");
        w.WriteLine($"{DateTime.Now:F} : {userInput} : {output}");
    }

    public void Read()
    {
        string historyData= File.ReadAllText(DataFileManager.ResourceFolder + _username + ".ElsaHistory");
        HistoryDisplay.Display(_username,historyData);

        //Process.Start($"notepad.exe", $"{DataFileManager.ResourceFolder+_username+".ElsaHistory"}");
    }
    
}