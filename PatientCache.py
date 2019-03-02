from Patient import *


class Cache:
    def __init__(self):
        self.file = open('cache.txt', 'at')
        self.file = open('cache.txt')
        patients = [line for line in self.file.read().split('\n')]
        self.patients = []
        for patient in patients:
            ssn = patient.split(':;')[1]
            a = Patient(ssn)
            self.patients.append(a)
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
