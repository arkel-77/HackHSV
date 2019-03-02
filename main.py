import Patient, PatientCache, GUI, DropDown
from Patient import*
from PatientCache import*
from GUI import*
from DropDown import*

#main render window
mainWindow = GUI("800x600")
#default dropdown selection name
unselected = "Select a patient"
#add patient name
add = "Add a patient (+)"
#patient list
patientCache = Cache()
#names list
names = [unselected, add]
#drop options
#def edit(ssn):
def add(ssn):
   patients.add_patient(ssn)
def combined_func(ssn,window):
   add(ssn)
   window.destroy()
   
def doStuff(var):
   print(var=="Add a patient (+)")
   if var=="Add a patient (+)":
      addScreen=Tk()
      addScreen.title("New Patient")
      SSNLabel = Label(addScreen,text="Enter Patient's SSN#: ")
      SSNLabel.grid(row=0,column=0)
      SSN=Entry(addScreen)
      SSN.grid(row=0,column=1)
      submit=Button(addScreen, text="submit",command=lambda:combined_func(SSN.get()))
      submit.grid(row=0,column=2)
      addScreen.mainloop()
selecter = dropDown(mainWindow,names,0,0)
while(1):
   if selecter.checkclicked():
      doStuff(selecter.selected.get())
   mainWindow.context.update_idletasks()
   mainWindow.context.update()
