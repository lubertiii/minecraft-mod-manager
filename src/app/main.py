#main program
#Dependencies
import sys                      #allows usage of functions related to the system
import os                       #allows usage of functions related to the operating system
from pathlib import Path        #allows usage of functions related to folder/file directory paths 
from script import folder_access #allows usage of the accessFolder function from the folder_access.py script
from script import mod_info

#Variables
username = os.getlogin()  #gets the username of the current user
folder_path = Path(fr"C:\Users\{username}\AppData\Roaming\.minecraft\mods") 

if __name__ == "__main__":
    mod_list = folder_access.accessFolder(folder_path)
    mod_info.modInfo(folder_path, mod_list)