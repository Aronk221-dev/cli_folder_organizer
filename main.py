# DONE: When the program runs, open a directory selection dialog

# TODO: Check if selected folder exists

# TODO: Check if the folder is not considered an important folder by the Windows Operating System
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
from tkinter import filedialog



class Fo_Parser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="Folder Organizer",
        )
        self.parser.add_argument(
            "cm",
            type=str,
            help="if 'cm' argument is given, the program will create a new folder called 'MISC', where everything that's not a file will be moved to."
        )
        self.args = self.parser.parse_args()
    
    def fo_parse_args(self):
        if self.args.cm == None:
            return False
        else:
            return True
            

def main():
    parser = Fo_Parser()
    
    directory = filedialog.askdirectory()
    
    if os.access(directory, os.F_OK):
        pass    
    

if __name__ == "__main__":
    main()