#main program
#Dependencies      
#allows usage of functions related to the operating system     
import os            
#allows usage of functions related to folder/file directory paths           
from pathlib import Path        
#allows usage of the accessFolder, modInfo, and versionCompatible function
from app.script import folder_access, mod_info, version_compatibility
import re

#Variables
username = os.getlogin()  #gets the username of the current user
folder_path = Path(fr"C:\Users\{username}\AppData\Roaming\.minecraft\mods") #mods folder path

if __name__ == "__main__":
    #minecraft version to be run
    minecraft_version = "26.3"
    #get all mods and its file path, store it in a list called mod_list
    mod_list = folder_access.accessFolder(folder_path)
    #get the minecraft version it is compatible with, store it in a list called version_list
    version_list = mod_info.modInfo(mod_list)
    #compile all evaluated compatibility of mods in a list called compatible_list
    compatible_list = version_compatibility.versionCompatible(version_list, minecraft_version)
    i = 0
    for compatible in compatible_list:    
        #mod_name = re.search(r"\\([^\\]+)\.jar$", str(mod_list[i]))
        #print(f"{mod_name.group(1)}: {compatible}")
        print(f"Compatible?: {compatible}")
        i += 1
