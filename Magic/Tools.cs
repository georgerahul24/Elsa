using System.IO;
using Newtonsoft.Json;




namespace Magic;


public class Json
{
    private readonly string _fileUrl;

    public Json(string fileUrl)
    {
        _fileUrl = fileUrl;
    }
   

    public T? Read<T>()
    {
        return JsonConvert.DeserializeObject<T>(File.ReadAllText(_fileUrl));
    }
        

   

    public void Write<TJsonType>(TJsonType jsonData) //Making the generic function to accept any kind of data
    {
        File.WriteAllText(_fileUrl, JsonConvert.SerializeObject(jsonData));
       
    }
}
