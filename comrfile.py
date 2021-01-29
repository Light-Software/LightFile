import zlib
import sys
import time
import os
from datetime import datetime
import ctypes
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile") #this is for the window title
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
File_ext = ".lfc"
chunksize = 1024




#if no extra arguments give the standard selection
if(len(sys.argv) == 1):
    print("Selected to compress.\nEnter the input file")
    path_total = input(": ")
    print("Enter the path to the output folder")
    output_path = input (": ")
else:
    path_total = sys.argv[1]
    output_path = getPath(sys.argv[2])

path = getPath(path_total)
file_name = getFileNameFromPath(path_total)
    
did_find_file = True
file_found_time = datetime.now

#change to the system root path

os.chdir(root_path)

#try changing to the path of the file

try:
    os.chdir(path)
except FileNotFoundError:
    print("Directory: {0} does not exist!".format(path))
    time.sleep(10)
except NotADirectoryError:
    print("{0} is not a directory!".format(path))
    time.sleep(10)
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))
    time.sleep(10)

#read the file

try:
    with open(file_name, 'rb') as str:
        while True:
            file_name = str.read(chunksize)
            if not file_name:
                break

    #no clue if this works, this needs testing

except FileNotFoundError:
    logging.critical('This file does not exist!')
    print("This file does not exist!")

start_time = time.time()

print("raw size:", sys.getsizeof(str))

compressed_data = zlib.compress(str, 9)

#change to the output location

did_compress = True

os.chdir(root_path)
os.chdir(output_path)

print("comppresed size:", sys.getsizeof(compressed_data))

#ask for name if not automated

if(len(sys.argv) == 1):
    print("Insert the new compressed file name") #if it's blank simply default it to compressed.lfc
    new_compr_fn = input(": ")
else:
    new_compr_fn = getFileNameFromPath(sys.argv[2])

if (new_compr_fn == ""):
    new_compr_fn = "compressed" #nothing was chosen so change the selected name to compressed, as we default do it

#create the file and write the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      to it

createfile = open(new_compr_fn + File_ext, 'w')
createfile.close()
savecomp = open(new_compr_fn + File_ext, 'wb')
savecomp.write(compressed_data)
savecomp.close()

did_save_compressed_file = True

app_root_path = getPath(abspath(getsourcefile(lambda:0)))

#history file
histfileopn = "history.lfh"

os.chdir(app_root_path)
current_datetime = datetime.now()
current_time = datetime.now().time()

# creating / opening the historu.lfh file

history = open(histfileopn, 'w')
history.write(path_total)
history.close()

#delete the file if the user wants.

if(len(sys.argv) == 1):
    print("do you want to delete the original file")
    delfile = input(": ")
else:
    delfile = "n"
    did_delete_file = False

if (delfile == "yes" or delfile == 'y' or delfile == "Y"):
    os.chdir(output_path)
    os.remove(file_name)
    did_delete_file = True

# print elapsed time
elapsed_time = time.time() - start_time
print("the compression took only:  ", round(elapsed_time),"sec" )

#get path for the documents folder
os.path.expanduser(documents)
os.chdir(documents_path)
if(path.exist(documents_path + "LightFileLogs")):
    #enter the directory
    os.chdir("lightFileLogs")
    logfile = logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    logfilesave = open("latest.txt", 'rw')
else:
    #create the directory for logs
    mkdir("LightFileLogs")
    os.chdir("lightFileLogs")
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    logfilesave = open("latest.txt", 'rw')


#wait 10 seconds and close if not run by commandline

if(len(sys.argv) == 1):
    print("compression successful app will close in 10 sec")
    time.sleep(10)


#EOF