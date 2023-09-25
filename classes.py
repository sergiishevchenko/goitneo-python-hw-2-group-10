from collections import UserDict

import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def validate(self, value):
        return re.match(r'(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+', value)


class Record:
    def __init__(self, name: Name, phone: Phone):
        self.name = name
        self.phones = [phone]

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)

    def find_phone(self, phone):
        if phone in self.phones:
            return phone

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # def __init__(self, data):
    #     self.data = data

    def add_record(self, record: Record):
        self[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return {name, self.data[name]}

    def delete(self, name):
        del self.data[name]