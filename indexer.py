import os
from multiprocessing import Process
from pathlib import Path

# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file

desktop = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
documents = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'))
downloads = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))
music = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'))
videos = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos'))
directories = ["C:\\Windows", desktop, documents, downloads, music, videos]

cache=open('cache.txt','w')

def index(pathn):
    try:
        for name in os.listdir(pathn):
            i = os.path.join(pathn, name)
            i = Path(i)
            if i.is_file() == True:
                print(i, name, sep=" !@#$%^& ")
                cache.write(f"{name} @#$%^& {i} \n")
            else:
                if name.startswith('.') == False and name.startswith('__') == False:
                    try:
                        index(i)
                    except Exception as e:
                        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    process = []
    for i in directories:
        print(i)
        p = Process(target=index, args=(i,))
        p.start()
        process.append(p)
'''
    for p in process:
        p.join()'''
