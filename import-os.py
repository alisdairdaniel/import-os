import os

targetDir = r'd:\tmp\util\dist\room'
files = []
dirs  = []


for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
    dirs += dirnames

print(files)
print(dirs)
