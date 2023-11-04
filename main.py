from datetime import datetime
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self._value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not Phone.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)
    @staticmethod
    def is_valid_phone(phone):
        pattern = r"^\+?\d{10}$|^\d{10}$"
        return bool(re.match(pattern, phone))


class Record:
    def __init__(self, name, birthday=None):
        self._name = Name(name)
        self._phones = []
        

    def add_phone(self, phone):
        phone = Phone(phone)
        self._phones.append(phone)

    def remove_phone(self, phone):
        self._phones = [p for p in self._phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not any(old_phone == p.value for p in self._phones):
            raise ValueError(f"Phone number '{old_phone}' does not exist.")
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self._phones:
            if p.value == phone:
                return p

    def __str__(self):
        phones = '; '.join(p.value for p in self._phones)
        return f"Contact name: {self._name.value}, phones: {phones}, birthday: {self._birthday.value if self._birthday else 'N/A'}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record._name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact '{name}' does not exist in the address book.")

    def iterator(self, N):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i + N]