# DONE: When the program runs, open a directory selection dialog

# DONE: Check if selected folder exists

# DONE: Check if the folder is not considered an important folder by the Windows Operating System
#           if it's considered an important folder -> 
#               - tell the user to select a different directory and reopen the dialog

# TODO: Optionally, if the program was run with the "-c_misc" argument: 
#           Create a folder called "MISC"

# TODO: Loop throught every item in the selected directory
# TODO:     if item is file: 
#               - find its extension
#               - add extension to a list, if said list doesn't yet contain the extension

 
# TODO:     if -c_misc was a given arg. and item doesn't begin with a ".": 
#               - if item is a folder -> move it to the MISC folder

import argparse
import os
from shutil import move as mv
from tkinter import filedialog



class Fo_Parser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="Folder Organizer",
        )
        self.parser.add_argument(
            "-cm",
            type=str,
            help="if '-cm' argument is given, the program will create a new folder called 'MISC', where everything that's not a file will be moved to.",
            default=None
        )
        self.args = self.parser.parse_args()
    
    def fo_parse_args(self):
        if self.args.cm == None:
            return False
        else:
            return True

important_folders:list = [
    "$SysReset",
    "Program Files",
    "Program Files (x86)",
    "ProgramData",
    "Users",
    "Windows",
    "XboxGames",
]

def valid_directory(dir:str) -> bool:
    if os.access(dir, os.F_OK) and dir.split('/')[-1] in important_folders:
        print(f"You probably shouldn't reorganize {dir}.")
        return False
    
    return True

def main():
    parser:Fo_Parser = Fo_Parser()
    
    directory:str = filedialog.askdirectory()
    
    while not valid_directory(directory):
        directory = filedialog.askdirectory()

    misc_dir_location:str = ""

    if parser.fo_parse_args() == True:
        os.mkdir(f"{directory}/MISC")
        misc_dir_location = f"{directory}/MISC"
    
    items_in_directory:list = os.listdir(directory)
    extensions_in_directory:list = []
    
    for item in range(len(items_in_directory)):
        if os.path.isdir(f"{items_in_directory[item]}") and item != misc_dir_location and misc_dir_location != "":
            mv(f"{items_in_directory[item]}", misc_dir_location)

    for item in range(len(items_in_directory)):
        if os.path.isfile(f"{items_in_directory[item]}"):
            extension = os.path.splitext(items_in_directory[item])[-1]
            extensions_in_directory.append(extension)
    
    print(extensions_in_directory)
        

        
    

if __name__ == "__main__":
    main()