import tkinter as tk
from menu import MenuBar
from toolbar import toolBar

class Application(tk.Tk):
   
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = MenuBar(self)
        tool = toolBar(self)
        self.config(menu=menubar)



        
app = Application()
app.mainloop()