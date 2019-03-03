from Patient import *


class Cache:
    def __init__(self):
        self.file = open('cache.txt', 'at')
        self.file = open('cache.txt')
        patients = [line for line in self.file.read().split('\n')]
        self.patients = []
        for patient in patients:
            try:
                ssn = patient.split(':;')[1]
                a = Patient(ssn)
                self.patients.append(a)
            except IndexError:
                pass
        self.file = open('cache.txt', 'at')

    def add_patient(self, patient: Patient):
        if patient not in self.patients:
            self.patients.append(patient)
            self.file.write('\n'+'SSN:;'+patient.ssn)
            for i in range(len(patient.attributeIndex)):
                self.file.write(';:'+patient.attributeIndex[i]+':;'+patient.valuesIndex[i])
            self.__init__()

    def get_patient(self, SSN: str):
        temp = [patient for patient in self.patients if patient.ssn == SSN]
        if len(temp) > 0:
            return temp[0]
        else:
            return None

    def delete_patient(self, patient: Patient):
        self.patients.remove(patient)
        file = open('cache.txt')
        file_data = file.read()
        file_data.replace('\nSSN:;'+patient.ssn,'')
        self.file = open('cache.txt','wt')
        self.file.write(file_data)
        self.__init__()

    def delete(self):
        self.file = open('cache.txt', 'wt')
        self.__init__()

    pass
