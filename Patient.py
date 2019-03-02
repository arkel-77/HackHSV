import os


class Patient:
    def __init__(self, SSN: str):
        try:
            self.file_read = open(SSN + '.txt')
        except:
            self.file_write = open(SSN + '.txt', 'at')
            self.file_write.write('SSN:;' + SSN)
            self.file_read = open(SSN + '.txt')
        self.ssn = SSN
        self.attributesAndValues = [line for line in self.file_write.read().split('\n')]
        self.attributedValues = [line.split(':;') for line in self.attributesAndValues]
        self.attributeIndex = [i[0] for i in self.attributedValues]
        self.valuesIndex = [i[1] for i in self.attributedValues]

    def get_attribute(self, attribute):
        if attribute in self.attributeIndex:
            return self.valuesIndex[self.attributeIndex.index(attribute)]
        else:
            return None

    def add_or_modify_attribute(self, attribute, value):
        if attribute not in self.attributeIndex:
            self.attributeIndex.append(attribute)
            self.valuesIndex.append(value)
            self.file_write.write('\n' + str(attribute) + ':;' + str(value))
        else:
            filedata = self.file_read.read()
            old_attval = attribute + ':;' + self.valuesIndex[self.attributeIndex.index(attribute)]
            new_attval = attribute + ':;' + value
            self.valuesIndex[self.attributeIndex.index(attribute)] = value
            filedata = filedata.replace(old_attval, new_attval)
            self.file_write = open(self.ssn + '.txt', 'wt')
            self.file_write.write(filedata)

    def delete(self):
        os.remove(self.ssn + '.txt')
        del self

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

    def all_attributes(self):
        for i in range(len(self.attributeIndex)):
            yield self.attributeIndex[i] + ':;' + self.valuesIndex[i]

    pass
