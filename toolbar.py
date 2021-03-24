
import tkinter as tk
from tkinter import filedialog
from helpers import read_file

class toolBar(tk.Tk):
	def __init__(self, master):
		myFrame = tk.Frame(master)
		# open file button + the icon
		self.openImg = tk.PhotoImage(file="images/folder1.png")
		self.openButton = tk.Button(myFrame , image=self.openImg , command=self.printing,borderwidth=1)
		self.openButton.pack(side=tk.LEFT ,padx=3)
		#save as button + the icon
		self.saveImg = tk.PhotoImage(file="images/floppy1.png")
		self.saveAsButton =tk.Button(myFrame , image=self.saveImg , command=self.printing ,borderwidth=1)
		self.saveAsButton.pack(side=tk.LEFT ,padx=3)
		# scale button + the icon
		self.scaleImg = tk.PhotoImage(file="images/scale.png")
		self.scaleButton = tk.Button(myFrame , image=self.scaleImg , command=self.printing,borderwidth=1)
		self.scaleButton.pack(side=tk.LEFT ,padx=3)

		self.zoomInImg = tk.PhotoImage(file="images/zoomIn.png")
		self.scaleButton = tk.Button(myFrame , image=self.zoomInImg , command=self.printing,borderwidth=1)
		self.scaleButton.pack(side=tk.LEFT ,padx=3)

		self.zoomOutImg = tk.PhotoImage(file="images/zoomOut.png")
		self.scaleButton = tk.Button(myFrame , image=self.zoomOutImg , command=self.printing,borderwidth=1)
		self.scaleButton.pack(side=tk.LEFT ,padx=3)

		
		myFrame.pack(side="top", fill=tk.X)

	def printing(self):
		print("clicked and working ")

