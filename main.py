from PatientCache import *
from GUI import *
from DropDown import *
from Editor import *

# main render window
mainWindow = GUI("800x600")
# default DropDown selection name
unselected = "Select a patient"
# add patient name
add = "I don't see my patient..."
# patient list
patientCache = Cache()
# names list
names = [unselected, add]
<<<<<<< HEAD
#drop options
def add(ssn):
   patientCache.add_patient(Patient(ssn))
def combined_func(ssn,window):
   add(ssn)
   window.destroy()
   edit(ssn)
def doStuff(var):
   print(var=="Add a patient (+)")
   if var=="Add a patient (+)":
      addScreen=Tk()
      addScreen.title("New Patient")
      SSNLabel = Label(addScreen,text="Enter Patient's SSN#: ")
      SSNLabel.grid(row=0,column=0)
      SSN=Entry(addScreen)
      SSN.grid(row=0,column=1)
      submit=Button(addScreen, text="submit",command=lambda:combined_func(SSN.get(),addScreen))
      submit.grid(row=0,column=2)
      addScreen.mainloop()
      
selecter = dropDown(mainWindow,names,0,0)
while(1):
   if selecter.checkclicked():
      doStuff(selecter.selected.get())
   mainWindow.context.update_idletasks()
   mainWindow.context.update()
=======


def edit(patient):
    return Editor(patient)


# drop options
def add(ssn):
    patientCache.add_patient(ssn)


def do_stuff(var):
    if var == add:
        add_screen = Tk()
        add_screen.title("New Patient")
        ssn_label = Label(add_screen, text="Enter Patient's SSN#: ")
        ssn_label.grid(row=0, column=0)
        ssn = Entry(add_screen)
        ssn.grid(row=0, column=1)
        submit = Button(add_screen, text="submit", command=lambda: add(ssn.get()))
        submit.grid(row=0, column=2)
        add_screen.mainloop()


selector = dropDown(mainWindow, names, 0, 0)
while True:
    if selector.checkclicked():
        do_stuff(selector.selected.get())
    mainWindow.context.update_idletasks()
    mainWindow.context.update()
>>>>>>> cc890eeda9b9a41899cbbc0598a63941d6e50861
