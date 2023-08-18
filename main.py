from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of the Record class")
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)


class Record:
    def __init__(self, name: Name, phones: Phone) -> None:
        self.name = name
        self.phones = [phone] if phones else []

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

    def days_to_birthday(self):
        pass

    def __repr__(self):
        return f"Data: {self.name}: {self.phones}"

    def __str__(self) -> str:
        return f"Name is {self.name}"


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"
    print("All Ok)")
