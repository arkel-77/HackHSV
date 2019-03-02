import sys, tkinter
from tkinter import*


class GUI:
    def __init__(self, param):  #GUI("800x600")
        #creating window obj
        self.context = Tk()
        self.context.title("HackHSV")
        #screen parameters
        self.context.geometry(param)
        #grid
        self.mainframe = Frame(self.context)
        self.mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
    #set loop
    def mainloop(self):
        self.context.mainloop()
    def setCloseAction(self, action):
        self.closeAction = action
    #def inp_handle(self):
    #def clear(self):
    #def draw(self, button):
    #def display(self):
