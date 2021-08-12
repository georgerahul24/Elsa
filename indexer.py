import os, webbrowser, talk1
from difflib import get_close_matches
from pathlib import Path
from functools import lru_cache
# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file
desktop = Path(os.path.join(os.path.join(os.environ['USERPROFILE']),
                            'Desktop'))
documents = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'))
downloads = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))
music = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'))
videos = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos'))
directories = [desktop, documents, downloads, music, videos]

cache = open('indexer.vira', 'w')


#enable cacging on index function to speed up the output
@lru_cache(maxsize=50, typed=False)
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


#TODO: Make a function call to index all file and store it in cache.vira
#TODO: Make a fumction call to search the elements use diflib module to find the nearby matches
#TODO: Remove the extensions while searching to make the life of user easier...Else user should input the extension also to get the sccurate results


def index_files():
    for paths in directories:
        index(paths)
    cache.close()


def search_indexed_file(filename):
    try:
        cache = open('indexer.vira', 'r')
        datas = cache.readlines()
        cache.close()
        cachedict = dict()
        filenames = []
        for data in datas:
            data = data.split(' @#$%^& ')
            cachedict[data[0]] = data[1]
            filenames.append(data[0])
        approx_file = get_close_matches(filename, filenames, n=1, cutoff=0.7)
        print(approx_file)
        if len(approx_file) != 0:
            srched_filepath = cachedict[approx_file[0]]
            webbrowser.open(srched_filepath)
            print(f'Opened {srched_filepath}')
            talk1.talk(f'Opened {approx_file[0]}')
        else:
            print(f'Could not find any files')
            talk1.talk(f'Could not find any files')
    except Exception as e:
        print('Error:', e)


#run index files when indexer module is imported in vira
index_files()

if __name__ == "__main__":
    index_files()
    while True:
        inp = input('Enter the filename: ')
        search_indexed_file(inp)
'''
if __name__ == "__main__":
    #...........sending the directories.............


    #...........opening the cache file..................
    cache = open("indexer.vira", "r")
    datas = cache.readlines()
    cachedict = dict()
    #.............read data to dictionary........
    for data in datas:
        data = data.split(' @#$%^& ')
        cachedict[data[0]] = data[1]

    print("Time convert filedata to dictionary:", time.perf_counter() - t1)
'''
