
namespace SearchBarGUI
{
    public static class StartUp
    {
        public static void Start()
        {
            Magic.DataFileManager.InitializeResourceFile();
            Magic.History history = new Magic.History("admin");
            history.Write("1", "2");
            history.Read();
        }
    }
}
