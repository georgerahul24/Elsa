import os
import time
from pathlib import Path

# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file
t = time.perf_counter()
desktop = Path(os.path.join(os.path.join(os.environ['USERPROFILE']),
                            'Desktop'))
documents = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'))
downloads = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))
music = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'))
videos = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos'))
directories = [desktop, documents, downloads, music, videos]

cache = open('cache.vira', 'w')


def index(pathn):
    try:
        for name in os.listdir(pathn):
            i = os.path.join(pathn, name)
            i = Path(i)
            if i.is_file() == True:
                print(i, name, sep=" !@#$%^& ")
                cache.write(f"{name} @#$%^& {i} @#$%^& \n")
            else:  #check for the files in a directories by calling the function recursively
                if name.startswith('.') == False and name.startswith(
                        '__') == False:
                    try:
                        index(i)
                    except Exception as e:
                        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    #...........sending the directories.............
    for i in directories:
        index(i)
    cache.close()
    t1 = time.perf_counter()
    print("Time taken to index files:", t1 - t)

    #...........opening the cache file..................
    cache = open("cache.vira", "r")
    datas = cache.readlines()
    cachedict = dict()
    #.............read data to dictionary........
    for data in datas:
        data = data.split(' @#$%^& ')
        cachedict[data[0]] = data[1]

    print("Time convert filedata to dictionary:", time.perf_counter() - t1)


#..........elizabeth.................... name of dictionary=cachedict
def file_search(name):
    pass
