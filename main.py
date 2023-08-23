from collections import UserDict
from datetime import datetime, timedelta
from dateparser import parse


def input_error(wrap):  # валідація
    def inner(
        *args,
    ):  # передаемо аргументи в інер -> то буде наш аргумент data в функціях на яких вuсить декоратор
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
        except ValueError:
            return "Give me an information"
        except KeyError:
            return "Give me the name from phonebook"

    return inner


class Field:
    def __init__(self, value) -> None:
        self.value = value

    # def __init__(self, name, birth_date):
    #     self.name = name
    #     self.birth_date = birth_date


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.name = value
        # self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.birthday = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = datetime.fromisoformat(self.birthday)

    # def validate(date_text):
    #     fmt = "%m.%d.%Y"
    #     try:
    #         d = datetime.strptime(date_text, fmt)

    #     except ValueError:
    #         return None
    #     else:
    #         return d# @classmethod

    # def validation(self, value):
    #     fmt = "%m.%d.%Y"
    #     try:
    #         birthday = datetime.strptime(value, fmt)
    #     except ValueError:
    #         return None
    #     else:
    #         return birthday

    # date = self.value.split(".")
    # self.birthday = datetime(date[0], date[1], date[2])
    # return self.birthday  # parse(self.value)


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

    @input_error
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
        this_year = (
            datetime(today.year, self.birthday.month, self.birthday.day) - today
        ).days
        if this_year >= 0:
            return this_year

        next_year = (
            datetime(today.year + 1, self.birthday.month, self.birthday.day) - today
        ).days
        return next_year

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
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    birthday = Birthday("22.12.1220")
    print(f"must be datetime obj: {birthday._birthday}")
    # print((rec.birthday))
    ab = AddressBook()
    ab.add_record(rec)
    # print(rec.days_to_birthday())
    # rec.days_to_birthday()

    # print((rec.name.value))

    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"
    print("All Ok)")


# # from datetime import datetime


# # def validate(date_text):
# #     fmt = "%m.%d.%Y"
# #     try:
# #         d = datetime.strptime(date_text, fmt)

# #     except ValueError:
# #         return None
# #     else:
# #         return d


# # v = validate("12.12.1277")
# # print(v)


# from datetime import date


# class Employee:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.birth_date = birth_date

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value.upper()

#     @property
#     def birth_date(self):
#         return self._birth_date

#     @birth_date.setter
#     def birth_date(self, value):
#         self._birth_date = date.fromisoformat(value)


# john = Employee("John", "2001-02-07")

# john.name
# print(john.birth_date)
# john.name = "John Doe"
# print(john.name)
