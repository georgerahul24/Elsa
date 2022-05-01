// See https://aka.ms/new-console-template for more information
using Theme;
theme _theme= new theme();
foreach (var theme in _theme.ThemeReader())
{
    Console.WriteLine(theme);
}
Console.ReadLine();