#File contains folder access algorithm
#Dependencies

#Function
def accessFolder(folder_path):
    #initialize list of file paths
    mod_list = []
    #iterate through all files in the folder
    for files in folder_path.iterdir():  
        #check if the current content is a file and is a .jar file
        if files.is_file() and files.suffix == ".jar":  
            #update each file path to the list
            mod_list.append(files)
            #print the name of the file
            #print(files.name)  
    
    return mod_list

