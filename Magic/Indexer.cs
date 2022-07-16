using System.Collections.Concurrent;
using System.Diagnostics;
using System.IO;

namespace Magic
{
    public static class Indexer
    {
        private static readonly Json Json = new("Data.Json");
        private static readonly ConcurrentDictionary<string, string> PathDictionary = new();

        public static int Index(string[] paths)
        {
            List<Thread> mainProcesses = new();
            foreach (string path in paths)
            {
                //Starting the threads
                Thread thread = new Thread(() => FindAllPaths(path));
                mainProcesses.Add(thread);
                Debug.WriteLine($"{thread.ManagedThreadId} started");
                thread.Start();
            }

            //Joining the threads
            foreach (Thread thread in mainProcesses)
            {
                thread.Join();
                Debug.WriteLine($"{thread.ManagedThreadId} stopped");
            }

            Json.Write(PathDictionary);
            PathDictionary.Clear(); //Resetting the dictionary
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
                        //Starting a new thread for each child directory
                        Thread childThread = new Thread(() => FindAllPaths(childPath));
                        childProcesses.Add(childThread);
                        childThread.Start();
                    }

                    foreach (string childPath in Directory.GetFiles(path))
                    {
                        //Indexing all the paths of the child files in it the directory
                        PathDictionary[Path.GetFileName(childPath)] = childPath;
                    }

                    foreach (Thread childThread in childProcesses)
                    {
                        //Stopping all the child threads
                        childThread.Join();
                    }
                }
                catch (UnauthorizedAccessException)
                {
                    Debug.WriteLine($"Access denied to {path}");
                }
            }
        }
    }
}