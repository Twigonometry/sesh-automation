import os
from pathlib import Path

#define the path to look in
target_dir = "basic-files"

#a directory that doesn't exist - try uncommenting this
# target_dir = "nonexistent"

#turn it into a 'Path' object
dir_path = Path(target_dir)

#check the directory exists
if not dir_path.is_dir():
    print("Directory doesn't exist - making it now!")
    dir_path.mkdir()

#get contents of all files in basic-files directory
for item in os.scandir(target_dir):
    #skip item if it's a directory
    if item.is_dir():
        continue

    #get the filepath
    filepath = Path(item)

    #open the file
    f = open(filepath)

    #read the contents
    for line in f:
        print(str(line))

    #close the file - remember to do this!
    f.close()