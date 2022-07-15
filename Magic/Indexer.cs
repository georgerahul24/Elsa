
using System.Collections.Concurrent;
using System.IO;
namespace Magic
{
    public static class Indexer
    {
       
        private static readonly Json Json = new("Data.Json");
        private static readonly ConcurrentDictionary<string, string> PathDictionary = new();
        public static int  Index(string[] paths)
        {
            
            List<Thread> mainProcesses = new();
            foreach (string path in paths)
            {
                //Starting the threads
                Thread thread = new Thread(()=>FindAllPaths(path));
                mainProcesses.Add(thread);
                Console.WriteLine($"{thread.ManagedThreadId} started");
                thread.Start();
                
            }
            //Joining the threads
            foreach (Thread thread in mainProcesses)
            {
                thread.Join();
                Console.WriteLine($"{thread.ManagedThreadId} stopped");
            }
            Json.Write(PathDictionary);
            PathDictionary.Clear();//Resetting the dictionary
            return 1;
        }
        private static void FindAllPaths(string path)
        {
            if (Directory.Exists(path))
            {
                List<Thread> childProcesses = new();
                try
                {
                    foreach (string childPath in Directory.GetDirectories(path))
                    {
                        Thread childThread = new Thread(()=>FindAllPaths(childPath));
                        childProcesses.Add(childThread);
                        childThread.Start();
                    }
                    foreach (string childPath in Directory.GetFiles(path))
                    {
                        PathDictionary[Path.GetFileName(childPath)] = childPath;
                    }

                    foreach (Thread childThread in childProcesses)
                    {
                        childThread.Join();
                    }
                }
                catch (UnauthorizedAccessException)
                {
                    Console.WriteLine($"Access denied to {path}");
                    
                }
                
            }
            

        }


    }

}

