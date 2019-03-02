from PatientCache import *
from GUI import *
from DropDown import *

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
