from GUI import *


class Editor(GUI):
    def __init__(self, patient, dimensions='800x600'):
        super().__init__(dimensions, title=patient.name + ' info')
        self.patient = patient
        self.changed = []
        self.textboxes = []
        for i in range(len(patient.attributedValues)):
            self.textboxes.append(TextBox(column=0,row=i,text=patient.attributedValues[i][0]))
            self.textboxes.append(TextBox(column=1, row=i, text=patient.attributedValues[i][1]))

    def save(self):
        for i in self.changed:
            self.patient.change_attribute(i[0], i[1])
