using Magic;

namespace MagicC;

public static class Data
{
    public static void Export()
    {

        File.WriteAllText("Backup.Elsa",File.ReadAllText(DataFileManager.ResourceFile));
    }
}