using Magic;

Usernames user = new Usernames();
Theme theme = new Theme();
foreach (var color in theme.ThemeReader())
{
    Console.WriteLine(color);
}




user.Write("hello","hi");
user.Write("hello","hi9iii");
user.Write("hllo","hi");

string input(string inpText)
{
    Console.Write(inpText);
    return Console.ReadLine();
}
while (true)
{
    string usr = input("Enter the username: ");
    string passwd = input("Enter the password: ");
    Console.WriteLine(user.Check(usr, passwd));
    
    
}


