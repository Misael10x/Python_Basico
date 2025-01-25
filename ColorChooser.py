from tkinter import *
from tkinter import colorchooser

def click():
   # color = colorchooser.askcolor()
   # colorHex = color[1]
    window.config(bg=colorchooser.askcolor()[1])
