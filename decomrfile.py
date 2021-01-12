#print("hello, world!")

import zlib
import sys
import time
import base64
import os
import ctypes
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile") # this is for the window title

#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and removes the file name (in this case, C:/Users/JohnDoe/Desktop)

def getPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    shouldAdd = False
    
    for c in reversedstr:
        if(shouldAdd == True):
            tempfn = tempfn + c
        if(c == '\\' or c == '/'):
            shouldAdd = True
        
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename

#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and returns just the file name (in this case, example.txt)

# s = string containing the path

def getFileNameFromPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    
    for c in reversedstr:
        if(c == '\\' or c == '/'):
            break
        tempfn = tempfn + c
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename

root_path = '/'
if(len(sys.argv) == 1):
    print("Selected to decompress.\nEnter the input file")
    path_total = input(": ")
    print("Enter the path to the output folder")
    output_path = input (": ")

    file_name  = getFileNameFromPath(path_total)
    path       = getPath(path_total)
else:
    path_total = sys.argv[1]
    output_path = getPath(sys.argv[2])
    
    file_name  = getFileNameFromPath(sys.argv[1])
    path       = getPath(sys.argv[1])


#File_rename = "no"
os.chdir(root_path)
try:
    os.chdir(path)
except FileNotFoundError:
    print("Directory: {0} does not exist!".format(path))
except NotADirectoryError:
    print("{0} is not a directory!".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))

str = open(file_name, 'rb').read()

#str = open('file_name', 'br')
try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("This file does not exist!")

time_start = time.time()

print("compressed size:", sys.getsizeof(str))

decompressed_data = zlib.decompress(str)
#zobj = zlib.decompressobj(str)  # obj for decompressing data streams that won’t fit into memory at once.
#this doesn't work :(

print("decomppresed size:", sys.getsizeof(decompressed_data))

os.chdir(root_path)
os.chdir(output_path)

if(len(sys.argv) == 1):
    print("Insert the new compressed file name")
    file_newname = input(": ")
else:
    file_newname = getFileNameFromPath(sys.argv[2])

#if nothing was inserted default to decompressed.txt
app_root_path =  getPath(abspath(getsourcefile(lambda:0)))
os.chdir(app_root_path) 
#open_hist = open( "history.lfh")
with open('history.lfh') as f:
    mylist = list(f)

os.chdir(root_path)
os.chdir(output_path) 

print(mylist[0])
filename = getFileNameFromPath(mylist[0])


if(file_newname == ""):
    file_newname = filename
os.chdir(app_root_path)
os.remove("history.lfh")
os.chdir(output_path)
#after reading the history file delete it
#now that i have that working i will use it as a temp file bc i have no clue how to read a specific like in a file 
#and internet tutorials aren't helping

#create the file and write to it

creaternfile = open(file_newname, 'w')
creaternfile.close()
savedecomp = open(file_newname, 'wb')
savedecomp.write(decompressed_data)
savedecomp.close()
if(len(sys.argv) == 1):
    print("do you want to delete the compressed file")

    delfile = input(": ")
else:
    delfile = "n"
    
if (delfile == "yes" or delfile == 'y' or delfile == "Y"):
    os.chdir(output_path)
    os.remove(file_name)
elif (delfile == "no" or delfile == 'n' or delfile == "N"):

    time_elapsed = time.time() - time_start

    print("decompression only took:", round(time_elapsed), "sec")
    if(len(sys.argv) == 1):
        print("decompression successful! app wil close in 10 sec")

        time.sleep(10)
