#File contains folder access algorithm
#Dependencies

#Functions
#Access Folder Function
def accessFolder(folder_path):
    mod_list = []
    for files in folder_path.iterdir():  #iterates through all files in the folder
        if files.is_file() and files.suffix == ".jar":  #checks if the current content is a file and is a .jar file
            mod_list.append(files)
            print(files.name)  #prints the name of the file
    
    return mod_list

