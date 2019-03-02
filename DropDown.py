import sys, tkinter
from tkinter import*
from GUI import*


class dropDown:
        
    def __init__(self, gui, array, Xpos, Ypos):
        self.confirmed=False
        self.selected = StringVar(gui.context)
        self.buttons = array
        self.selected.set(self.buttons[0])#default val

        self.popupMenu = OptionMenu(gui.mainframe, self.selected, *(self.buttons))
        self.popupMenu.grid(column=Xpos,row=Ypos)

        def setclicked():
            self.confirmed = True
        
        self.okay = Button(gui.context,text="confirm",width=10,command=setclicked)
        self.okay.grid(column=Xpos,row=Ypos+1)
            
    def checkclicked(self):
        ret = self.confirmed
        self.confirmed = False
        return ret

    def add(self,var):
        self.buttons.insert(len(self.buttons)-1,var)
