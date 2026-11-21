#File contains mod metadata information such as, version, and applicable minecraft version
#Dependencies
#allows usage of zipfile to open zip files and read its data
import zipfile
#allows manipulation of json files
import json

#Function
def modInfo(mod_list: list):
    #intialize list for compilation of compatible minecraft versions
    version_list = []
    #iterate through each mod file path
    for each_mod in mod_list:
        #read each mod .jar file
        with zipfile.ZipFile(each_mod, "r") as jar_metadata:
            #check if fabric.mod.json in metadata namelist
            if "fabric.mod.json" in jar_metadata.namelist():
                #read info on fabric.mod.json metadata and store it in "info" variable
                info = json.loads(jar_metadata.read("fabric.mod.json").decode("utf-8"), strict=False)

                #mod_version = info.get("version", "Unknown")
                #get the compatible minecraft version for each mod on the list. ("*") at the end refers to any version if the mod does not indicate version
                raw_minecraft_version = info.get("depends", {}).get("minecraft", "*")
                #check if raw_minecraft_version output is a string, if not, convert to string
                string_minecraft_version = convert(raw_minecraft_version)
                #update each compatible version of every mod to the version list
                version_list.append(string_minecraft_version)
                #print(minecraft_version)
    
    return version_list

def convert(raw_minecraft_version):
    #check if the version value is in string data type or list, if it is a list, convert the list into a string 
    if isinstance(raw_minecraft_version, str):
        #if the value is a string, just return the value without changing it
        return raw_minecraft_version
    else:
        #if the value is a list, convert it into a string by joining the elements inside the list
        return ",".join(raw_minecraft_version)