#File contains folder access algorithms
#Dependencies

#Functions
#Access Folder Function
def accessFolder(folder_path):
    for files in folder_path.iterdir():  #iterates through all files in the folder
        if files.is_file() and files.suffix == ".jar":  #checks if the current content is a file and is a .jar file
            print(files.name)  #prints the name of the file

