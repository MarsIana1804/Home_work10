from collections import UserDict


class Field:
    def __init__(self, val: str): 
        self.value = val

class Name(Field):
    pass
     
class Phone(Field):
    pass
    


class Record():

    def __init__(self, n: Name, ph: Phone=None) -> None:
        self.name = n
        
        self.phones = []
        if ph:
            self.add_phone_object(ph)

    def add_phone_object(self, ph_n: Phone):
        self.phones.append(ph_n)
    
    def remove_phone_obj(self, phone_obj: Phone):
        self.phones.remove(phone_obj)

    def edit_phone_obj(self, new_number: str, i):
        self.phones[i].value = new_number


class AddressBook(UserDict):
        
    def add_record(self, rec: Record):
        
        self.data[rec.name.value] = rec




if __name__ == '__main__':

    name = Name('Bill')
    phone = Phone('1234567890')
    new_phone = Phone('36367647637')
    #phone_number3 = Phone('5555555555')
    rec = Record(name, phone)

    rec.add_phone_object(new_phone)
    print(rec.phones)
    print(rec.phones[1].value)
    rec.edit_phone_obj('5555555555', 1)
    print(rec.phones[1].value)
    rec.remove_phone_obj(new_phone)
    print(rec.phones)




    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
    print(rec.name.value)
    print(ab["Bill"].phones)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')

    







