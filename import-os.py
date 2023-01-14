import os

targetDir = r'd:\tmp\util\dist\room'
files = []
dirs  = []

def dir_how():
    for (dirpath, dirnames, filenames) in os.walk(targetDir):
        files += filenames
        dirs += dirnames

    print(files)
    print(dirs)
aaa = dir_how()
