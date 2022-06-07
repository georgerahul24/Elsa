using HistoryGUI;
namespace Magic;

public class History

{
    private readonly string _username;
    private readonly DataFileManager _dataFileManager;

    public History(string username)
    {
        _username = username;
        _dataFileManager = new DataFileManager(_username);
    }
    public void Write(string userInput,string output)
    { 
        //This file is to save the history to user file
        
        _dataFileManager.Write("History",$"{DateTime.Now:F} : {userInput} : {output}");
    }

    public void Read()
    {
        string st = string.Join("\r\n", _dataFileManager.GetHistory());
        HistoryDisplay.Display(_username,st);

        //Process.Start($"notepad.exe", $"{DataFileManager.ResourceFolder+_username+".ElsaHistory"}");
    }
    
}