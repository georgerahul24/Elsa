using System.Drawing;
using System.Text.Json;
using Magic;
using System.Collections.Generic;
Json json = new Json();
List<string> li = new List<string> { "#000bbb","#123456","#12435a" };
json.Write(Locations.ThemeFile,li);


Theme theme = new Theme();
foreach (Color color in theme.ThemeReader()!)
{
    Console.WriteLine(color);
}

