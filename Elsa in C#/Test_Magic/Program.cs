// See https://aka.ms/new-console-template for more information
using Magic;
using System.Text.Json;
using System.Collections.Generic;
/*
 Dictionary<string,string> dictionary= new Dictionary<string,string>(){{"GR","1234"}};
 string? jsonobj = JsonSerializer.Serialize(dictionary);
 Usernames user = new Usernames();
 File.WriteAllText(user.fileURL,jsonobj);
 Console.Write(jsonobj);
*/
Usernames user = new Usernames();
Theme theme = new Theme();
foreach (var color in theme.ThemeReader())
{
    Console.WriteLine(color);
}


user.write("hello","hi");
user.write("hello","hi9iii");
user.write("hllo","hi");
