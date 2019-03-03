from GUI import *
from tkinter.scrolledtext import*

class Editor(GUI):

    def __init__(self, patient, dimensions='800x1400'):
        super().__init__(dimensions, title=patient.name + ' info')
        self.patient = patient
        self.addField = Button(self.context,text="Add field",command=self.add_field).grid(row=0,column=2)
        self.delete = Button(self.context,text="Delete from records").grid(row=1,column=2)
        self.labels = []
        self.entries = []
        for i in range(len(patient.attributeIndex)):
            self.labels.append(Label(self.context,text=patient.attributeIndex[i]+": ").grid(row=i,column=0))
            if patient.attributeIndex[i] == 'Schedule' or patient.attributeIndex[i] == 'Current Medicines' or patient.attributeIndex[i] == 'Medical History':
                self.entries.append(ScrolledText(self.context, height=1).grid(row=i,column=1))
            else:
                self.entries.append(Entry(self.context,textvariable=StringVar(self.context,value=patient.valuesIndex[i])).grid(row=i,column=1))
    def add(self,field,screen):
        self.patient.assert_attribute(field)
        self.labels.append(Label(self.context,text=field+": ").grid(row=len(self.patient.attributeIndex)-1,column=0))
        self.entries.append(Entry(self.context,textvariable=StringVar(self.context,value=self.patient.valuesIndex[len(self.patient.attributeIndex)-1])).grid(row=len(self.patient.attributeIndex)-1,column=1))
        self.addField.destroy()
        screen.destroy()
    def add_field(self):
        add_screen = Tk()
        add_screen.title("New Field")
        field_label = Label(add_screen, text="Field Name: ")
        field_label.grid(row=0, column=0)
        field = Entry(add_screen)
        field.grid(row=0, column=1)
        submit = Button(add_screen, text="submit", command=lambda: self.add(field.get(),add_screen))
        submit.grid(row=0, column=2)
        add_screen.mainloop()
    def save(self):
        for i in range(len(patient.attributeIndex)):
            patient.change_attribute(patient.attributeIndex[i],entries[i].get())
        
