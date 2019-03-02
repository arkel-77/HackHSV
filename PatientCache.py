from Patient import *


class Cache:
    def __init__(self):
        self.file = open('cache.txt', 'at')
        self.file = open('cache.txt')
        self.patients = [line for line in self.file.read().split('\n')]
        self.patients = [line.split(':;') for line in self.patients]
        self.ssns = [patient[1] for patient in self.patients]
        self.patients = [Patient(ssn) for ssn in self.ssns]
        self.file = open('cache.txt', 'at')

    def add_patient(self, patient):
        self.patients.append(patient)
        self.file.write(patient.name + ':;' + patient.ssn)

    def get_patient(self, name=None, SSN=None):
        if name is None:
            temp = [patient for patient in self.patients if patient.ssn == SSN]
        else:
            temp = [patient for patient in self.patients if patient.name == name]
        return temp[0]
