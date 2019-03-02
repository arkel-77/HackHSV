class Patient:
    def __init__(self, SSN: str):
        self.file = open(SSN+'.txt', 'at')
        self.file = open(SSN+'.txt')
        self.ssn = SSN
        self.attributesAndValues = [line.split(':;') for line in self.file.read().split('\n')]
        self.attributeIndex = [i[0] for i in self.attributesAndValues]
        self.valuesIndex = [i[1] for i in self.attributesAndValues]
        self.file = open(SSN+'.txt', 'at')

    def get_attribute(self, attribute):
        if attribute in self.attributeIndex:
            return self.valuesIndex[self.attributeIndex.index(attribute)]
        else:
            return None

    def add_attribute(self, attribute, value):
        if attribute not in self.attributeIndex:
            self.attributeIndex.append(attribute)
            self.valuesIndex.append(value)
            self.file.write('\n'+str(attribute) + ':;' + str(value))
