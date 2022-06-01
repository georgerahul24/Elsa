using Magic;
using System.IO;

namespace Magic;

public static class Data
{
    public static void Export()
    {

        File.WriteAllText("Backup.Elsa",File.ReadAllText(DataFileManager.ResourceFile));
    }
}