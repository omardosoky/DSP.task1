import tkinter as tk
from tkinter import Menu
from tkinter import filedialog
from helpers import read_file
import sys


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="new file",  command=self.browse_files)
        fileMenu.add_command(label="save as",  command=self.browse_files)
        fileMenu.add_separator() 
        fileMenu.add_command(label="Exit",  command=self.quit)

    def browse_files(self):
            filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                        ("all files",
                                                            "*.*")))        
            if filename is not None:
                self.content = read_file(filename)
                self.parent.event_generate("<<Fileread>>")
                # print(self.content)
    def quit(self):
            sys.exit(0)






   