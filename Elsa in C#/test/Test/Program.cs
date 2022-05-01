using Theme;

Console.WriteLine("Hello, World!");
theme _Theme = new theme();
foreach (var _theme in _Theme.ThemeReader())
{
    Console.WriteLine(_theme);
}
