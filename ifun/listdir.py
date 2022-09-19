from os import listdir
from os.path import isfile, isdir, join

path = '/var/log'

files = listdir(path)

for f in files:
    fullpath = join(path, f)
    if isfile(fullpath):
        print('File:', f)
    elif isdir(fullpath):
        print('Folder:', f)
