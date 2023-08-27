from collections import UserDict
from datetime import date
import re


class Field:
    def __init__(self, value) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value

    def __str__(self) -> str:
        return f"{self.value}"

    def __eq__(self, new_value) -> bool:
        if isinstance(new_value, self.__class__):
            return self.value == new_value.value


class Name(Field):
    @Field.value.setter
    def value(self, name: str):
        if not name.isalpha():
            raise ValueError("not valid name only alpha")
        Field.value.fset(self, name)
        # super(Name, Name).value.fset(self, name)


class Phone(Field):
    def __valid_phone(self, phone: str) -> None:
        if not isinstance(phone, str):
            raise ValueError("only str for number")
        if not phone.isdigit():
            raise ValueError("Error... Phone number must be digit")

    @Field.value.setter
    def value(self, phone: str):
        self.__valid_phone(phone)
        Field.value.fset(self, phone)


class Birthday(Field):
    def __valid_date(self, birthday: str) -> None:
        try:
            date.fromisoformat(birthday)
        except ValueError:
            raise ValueError("invalid format date, only ISO format yyyy-mm-dd")

    @Field.value.setter
    def value(self, birthday):
        self.__valid_date(birthday)
        Field.value.fset(self, birthday)

    def get_date(self):
        return date.fromisoformat(self.value)


class Record:
    def __init__(self, name: Name, phone: Phone, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def del_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone not in self.phones:
            # перевірка на входження (порівнюемо строку зі строками - все коректно без додаткових магічних методів)
            raise ValueError(f"old...{old_phone}")
        if new_phone not in self.phones:
            raise ValueError(f"new {new_phone}")
        index = self.phones.index(old_phone)
        # знаходимо індекс..індекси у списку обьектів і у списку строк відповідні
        self.phones[index] = new_phone

    # змінюемо значення обьекту при цьому комірка памьяті залишаеться та сама у обьекту Phone

    def days_to_birthday(self) -> int:
        today = date.today()
        b_day = self.birthday.get_date().replace(year=today.year)
        if b_day < today:
            b_day = b_day.replace(year=today.year + 1)
        return (b_day - today).days


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of the Record class")
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)
    
    # def iterator(self, item_number: int) -> str:

    # def __iter__(self):
    #     # return Iterable()
    #     pass


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("39447509105")
    bday = Birthday("1234-12-12")

    record = Record(name, phone, bday)
    print(record.)
