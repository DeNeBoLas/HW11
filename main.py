from collections import UserDict
from datetime import date
import itertools


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
        # if type(record) != Record:
        #     raise TypeError("")
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    # def __next__(self): # TODO  як резалізувати вивід даних через  __next__ та __iter__
    #     if n < len(self.data):
    #         n += 1
    #         return self.data[record.name.value]
    #     raise StopIteration

    # def __iter__(self):
    #     return AddressBook()

    # def chunks(seq, n):
    #     it = iter(seq)
    #     while True:
    #         t = tuple(itertools.islice(it))
    #         if len(t) == 0:
    #             break
    #         yield t

    def iterator(self) -> tuple:
        return f"{self.data}"

    # for c in chunks(self.data.items, n):
    #     yield c

    # def __iter__(self):
    #     return chunks()


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("39447509105")
    bday = Birthday("1234-12-12")

    name_1 = Name("Tom")
    phone_1 = Phone("39447509105")
    bday_1 = Birthday("1234-12-12")

    name_2 = Name("Ket")
    phone_2 = Phone("39447509105")
    bday_2 = Birthday("1234-12-12")

    name_3 = Name("Gim")
    phone_3 = Phone("7654689")
    bday_3 = Birthday("1298-10-17")

    record = Record(name, phone, bday)
    record_1 = Record(name_1, phone_1, bday_1)
    # record.add_phone("2345657")
    record_2 = Record(name_2, phone_2, bday_2)
    record_3 = Record(name_3, phone_3, bday_3)
    print(record.name, [p.value for p in record.phones], record.birthday)

    ab = AddressBook()
    ab.add_record(record)
    ab.add_record(record_1)
    ab.add_record(record_2)
    ab.add_record(record_3)
    print(ab.data)

    for el in ab:  # TODO як вивести номер та др
        print(el)
