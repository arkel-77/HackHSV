import os


class Patient:
    def __init__(self, SSN: str):
        self.file_write = open(SSN + '.txt', 'at')
        self.file_read = open(SSN + '.txt')
        self.ssn = SSN
        self.attributesAndValues = [line for line in self.file_read.read().split(',^')]
        self.attributedValues = [line.split(':;') for line in self.attributesAndValues]
        try:
            self.attributeIndex = [i[0] for i in self.attributedValues]
            self.valuesIndex = [i[1] for i in self.attributedValues]
        except IndexError:
            self.attributeIndex = []
            self.valuesIndex = []

        self.assert_attribute('SSN', SSN)
        self.assert_attribute('First Name')
        self.assert_attribute('Last Name')
        self.assert_attribute('Medical History')
        self.assert_attribute('Birth Date')
        self.assert_attribute('Current Medicines')
        self.assert_attribute('Schedule')

    def change_attribute(self, attribute: str, value: str):
        if attribute not in self.attributeIndex:
            self.attributeIndex.append(attribute)
            self.valuesIndex.append(value)
            self.file_write.write(',^' + str(attribute) + ':;' + str(value))
        else:
            file_data = self.file_read.read()
            old_attval = attribute + ':;' + self.valuesIndex[self.attributeIndex.index(attribute)]
            new_attval = attribute + ':;' + value
            self.valuesIndex[self.attributeIndex.index(attribute)] = value
            file_data = file_data.replace(old_attval, new_attval)
            self.file_write = open(self.ssn + '.txt', 'wt')
            self.file_write.write(file_data)
        self.file_read = open(self.ssn + '.txt')

    def assert_attribute(self, attribute: str, default: str=' '):
        if self.get_attribute(attribute) is None:
            self.change_attribute(attribute, default)
        self.file_read = open(self.ssn + '.txt')

    def delete(self):
        os.remove(self.ssn + '.txt')
        del self

    def remove_attribute(self, attribute: str):
        file_data = self.file_read.read()
        old_val = self.valuesIndex[self.attributeIndex.index(attribute)]
        old_attval = attribute + ':;' + old_val
        file_data = file_data.replace(',^' + old_attval, '')
        self.file_write = open(self.ssn + '.txt')
        self.file_write.write(file_data)
        self.__init__(self.ssn)

    def get_attribute(self, attribute: str):
        if attribute in self.attributeIndex:
            return self.valuesIndex[self.attributeIndex.index(attribute)]
        else:
            return None

    @property
    def name(self):
        fn = self.get_attribute('First Name')
        mn = self.get_attribute('Middle Name')
        ln = self.get_attribute('Last Name')
        if mn is not None:
            if fn is not None:
                if ln is not None:
                    return fn + ' ' + mn + ' ' + ln
                else:
                    return fn + ' ' + mn
            else:
                if ln is not None:
                    return mn + ' ' + ln
                else:
                    return mn
        else:
            if fn is not None:
                if ln is not None:
                    return fn + ' ' + ln
                else:
                    return fn
            else:
                if ln is not None:
                    return ln
                else:
                    return ''

    pass

