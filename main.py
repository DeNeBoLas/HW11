from collections import UserDict
from datetime import datetime, timedelta
from dateparser import parse
import re
import phonenumbers


# def input_error(wrap):  # валідація
#     def inner(
#         *args,
#     ):  # передаемо аргументи в інер -> то буде наш аргумент data в функціях на яких вuсить декоратор
#         try:
#             return wrap(*args)
#         except IndexError:
#             return "Give me name and phone please"
#         except ValueError:
#             return "Give me an information"
#         except KeyError:
#             return "Give me the name from phonebook"

#     return inner


class Field:
    def __init__(self, value) -> None:
        self.value = value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def name(self, new_value: str):
        self.__value = new_value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__name = None
        self.name = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception("Wrong name")


class Phone(Field):
    def __init__(self, value: str) -> None:
        self.phone = value
        super().__init__(value)
        self.__phone = None

    @property
    def is_valid_phone(self):
        return self.__phone

    @is_valid_phone.setter
    def is_valid_phone(self, phone: str):
        p = phonenumbers.parse(phone, None)
        if phonenumbers.is_valid_number(p):
            self.__phone = p
            # print(type(p))
        else:
            raise Exception("Wrong number")


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.birthday = value

    @property
    def birthday(self):
        return self.birthday

    @birthday.setter
    def birthday(self, value):
        self.bd = datetime.fromisoformat(value)
        return self.bd


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of the Record class")
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)


class Record:
    def __init__(self, name: Name, phones: Phone, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = [phone] if phones else []
        self.birthday = birthday

    # @input_error
    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def del_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        phones_str = [
            ph.value for ph in self.phones
        ]  # створюемо список який містить значення телефонів (стр) а не обьекти Phone
        if (
            old_phone not in phones_str
        ):  # перевірка на входження (порівнюемо строку зі строками - все коректно без додаткових магічних методів)
            raise ValueError
        index = phones_str.index(
            old_phone
        )  # знаходимо індекс..індекси у списку обьектів і у списку строк відповідні
        self.phones[
            index
        ].value = new_phone  # змінюемо значення обьекту при цьому комірка памьяті залишаеться та сама у обьекту Phone

    # @input_error
    def days_to_birthday(
        self,
    ):
        today = datetime.now()
        self.birthday = Birthday.birthday
        if self.birthday < today:
            my_birthday = my_birthday.replace(year=today.year + 1)
        time_to_birthday = abs(my_birthday - today)

        return time_to_birthday.days

    # this_year = (
    #     datetime(today.year, self.birthday.month, self.birthday.day) - today
    # ).days
    # if this_year >= 0:
    #     return this_year

    # next_year = (
    #     datetime(today.year + 1, self.birthday.month, self.birthday.day) - today
    # ).days
    # return next_year

    # next_year = today + timedelta(years=1)

    # delta1 = datetime(today, today.month, today.day)
    # delta2 = datetime(today.year + 1, self.birthday.month, self.birthday.day)

    # return ((delta1 if delta1 > today else delta2) - today).days

    # birthdays_in_this_year = user["birthday"].replace(year=today.year)
    # if today <= birthdays_in_this_year < next_year:
    #     birthday = next_year - today
    # return birthday

    def __repr__(self):
        return f"Data: {self.name}: {self.phones}"

    def __str__(self) -> str:
        return f"Name is {self.name}"


if __name__ == "__main__":
    # name = Name("Bill")
    # print(name.value)

    phone = Phone("+2345698")
    print(phone.is_valid_phone)

    birthday = Birthday("2002-12-04")
    b = Birthday("1212-12-12")
    print(f"must be datetime obj:{(b.bd.date())}")

    # rec = Record(name, phone)

    # rec.days_to_birthday
    # print(rec.days_to_birthday())

    # print((rec.birthday))

    ab = AddressBook()
    # ab.add_record(rec)
    # print(rec.days_to_birthday())
    # rec.days_to_birthday()

    # print((rec.name.value))

    # assert isinstance(ab["Bill"], Record)
    # assert isinstance(ab["Bill"].name, Name)
    # assert isinstance(ab["Bill"].phones, list)
    # assert isinstance(ab["Bill"].phones[0], Phone)
    # assert ab["Bill"].phones[0].value == "+1234567890"
    print("All Ok)")


# def validate(date_text):
#     fmt = "%m.%d.%Y"
#     try:
#         d = datetime.strptime(date_text, fmt)

#     except ValueError:
#         return None
#     else:
#         return d
#
# # @classmethod

# def validation(cls, value):
#     fmt = "%m.%d.%Y"
#     try:
#         birthday = datetime.strptime(cls.value, fmt)
#     except ValueError:
#         return None
#     else:
#         return birthday

# date = cls.value.split(".")
# self.birthday = datetime(date[0], date[1], date[2])
# return self.birthday  # parse(self.value)
