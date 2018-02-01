class AddrBookEntry(object):
    'address book entry class'
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def updatePhone(self, phone):
        self.phone = phone


tom = AddrBookEntry('Tom', 12345678)
print('%s phone num is %d' % (tom.name, tom.phone))



class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, name, phone, id, email):
        AddrBookEntry.__init__(self, name, phone)
        self.id = id
        self.email = email

    def updateEmail(self, email):
        self.email = email



jone = EmplAddrBookEntry('Jone', 123456789, 2001, 'jone@gmail.com')
jone.updateEmail('jone02@gmail.com')
print('hello, %s, your id is %d, phone num is %d, email is %s' % (jone.name, jone.id, jone.phone, jone.email))
