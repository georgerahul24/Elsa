
using System.Collections.Concurrent;
using System.IO;
namespace Magic
{
    public static class Indexer
    {
        public static ConcurrentDictionary<string,string> Index(string[] paths)
        {
            ConcurrentDictionary<string, string> PathDictionary = new();
            foreach (string path in paths)
            {
                FindAllPaths(path, ref PathDictionary);
            }

            return PathDictionary;
        }
        private static void FindAllPaths(string path, ref ConcurrentDictionary<string, string> PathDictionary)
        {
            if (Directory.Exists(path))
            {
                
                foreach (string childPath in Directory.GetDirectories(path))
                {
                    FindAllPaths(childPath, ref PathDictionary);
                }
                foreach (string childPath in Directory.GetFiles(path))
                {
                    PathDictionary[Path.GetFileName(childPath)] = childPath;
                }
            }
            

        }


    }

}

