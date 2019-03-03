from tkinter import *


class GUI:
    def __init__(self, param, title=''):
        # creating window object
        self.context = Tk()
        self.context.title(title)
        # screen parameters
        self.context.geometry(param)
        # grid
        self.mainframe = Frame(self.context)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

    # set loop

    def mainloop(self):
        self.context.mainloop()
