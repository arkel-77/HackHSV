from Patient import *


class Cache:
    def __init__(self):
        self.file = open('cache.txt', 'at')
        self.file = open('cache.txt')
        patients = [line for line in self.file.read().split('\n')]
        patients = [line.split(';:') for line in patients]
        self.patients = []
        for patient in patients:
            temp = [attval.split(':;') for attval in patient]
            try:
                ssn = temp[0][1]
                a = Patient(ssn)
                for attval in temp[1:]:
                    a.add_or_modify_attribute(attval[0], attval[1])
                self.patients.append(a)
            except IndexError:
                pass
        self.file = open('cache.txt', 'at')

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        self.file.write('\n'+'SSN:;'+patient.ssn)
        for i in range(len(patient.attributeIndex)):
            self.file.write(';:'+patient.attributeIndex[i]+':;'+patient.valuesIndex[i])

    def get_patient(self, SSN: str):
        temp = [patient for patient in self.patients if patient.ssn == SSN]
        if len(temp) > 0:
            return temp[0]
        else:
            return None

    def delete(self):
        self.file = open('cache.txt', 'wt')
        self.__init__()

    pass
