#File contains mod metadata information such as, version, and applicable minecraft version
import zipfile
import json

def modInfo(folder_path, mod_list):
    for each_mod in mod_list:
        with zipfile.ZipFile(each_mod, "r") as jar_metadata:
            if "fabric.mod.json" in jar_metadata.namelist():
                info = json.loads(jar_metadata.read("fabric.mod.json").decode("utf-8"), strict=False)

                mod_version = info.get("version", "Unknown")
                minecraft_version = info.get("depends", {}).get("minecraft", "Any")
                mod_info = [mod_version, minecraft_version]
                print(mod_info)