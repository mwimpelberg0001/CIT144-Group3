try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class transferGUI():
    def __init__(self):
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        
        
