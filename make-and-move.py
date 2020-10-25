import sys
import subprocess
from pathlib import Path

#get number of files to make
quantity = 0

try:
    quantity = int(sys.argv[1])
except:
    print("Please supply an integer parameter")
    sys.exit()

print(quantity)

#use subprocess to make file
for i in range(quantity):
    filename = "move-me-" + str(i) + ".txt"
    subprocess.check_call(['touch', filename])

#check directory exists - create it if not
dir_path = Path("get-in-here")

if not dir_path.is_dir():
    dir_path.mkdir()

#subprocess to move txt files
#could put this code in the same loop as before to improve efficiency, but kept separate for clarity
for i in range(quantity):
    filename = "move-me-" + str(i) + ".txt"
    subprocess.check_call(['mv', filename, "get-in-here"])