
using Magic;


namespace SearchBarGUI
{
    public static class StartUp
    {
        public static void Start()
        {
            DataFileManager dataFileManager = new Magic.DataFileManager("admin");
            dataFileManager.InitializeResourceFile();
            History history = new History("admin");
            history.Write("1", "2");
            history.Read();


        }
    }
}
