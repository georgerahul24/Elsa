using System.Drawing;
using Magic;
using MagicC;

//Console.WriteLine(DataFileManager.InitializeResourceFile());
Usernames user=new Usernames();
History history = new History("admin");
history.Write("Hello","hi");
history.Read();
user.Write("Admin","123");
Console.WriteLine(user.Check("Admin", "3141"));
Console.WriteLine(user.Check("Admin", "123"));

Theme theme = new Theme();
foreach (Color color in theme.ThemeReader()!)
{
    Console.WriteLine(color);
}

