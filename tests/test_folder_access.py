from src.app.script import folder_access
from pathlib import Path
import os


#Variables
username = os.getlogin()  #gets the username of the current user
folder_path = Path(fr"C:\Users\{username}\AppData\Roaming\.minecraft\mods")

if __name__ == "__main__":
    folder_access.accessFolder(folder_path)