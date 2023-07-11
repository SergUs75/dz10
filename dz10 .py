from collections import UserDict


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return wrapper


def hello():
    return 'How can I help you?'


@input_error
def no_comand(*args):
    return 'Unknown command'


class Field:
    pass
    

class Name(Field):
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return self.name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
    def __str__(self):
        return self.phone
    def __repr__(self):
        return str(self.phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone]
    def __str__(self):
        return str(self.phones)
    def __repr__(self):
        return str(self.phones)


    @input_error
    def add_phone(self, name, phone):
        print(name)
        print(phone)
        print(address_book)
        if name in address_book:
            print(1)
            record = address_book[name]
            phone = Phone(phone)
            record.phones.append(phone)
            return f'Add {name}: {phone}'
    

    @input_error
    def delete_phone(self, name, phone):
        if name in address_book:
            record = address_book[name]
            phone = Phone(phone)
            for i in record.phones:
                if phone.phone == i.phone:
                    record.phones.remove(i)
                    return f'Deleted {phone} from {name}'


    @input_error
    def edit_phone(self, name, phone):
        old_phone = Phone(phone[0])
        new_phone = Phone(phone[1])
        if name in address_book:
            record = address_book[name]
            for i in record.phones:
                if old_phone.phone == i.phone:
                    record.phones.remove(i)
                    record.phones.append(new_phone)
                    return f'Updated {name}: {old_phone} -> {new_phone}'


@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    
    record = Record(name, phone)
    address_book.add_record(record)
    return f'Add {record.name}: {record.phones}'


@input_error
def change(*args):
    name = args[0]
    phone = args[1]
    if name in address_book:
        address_book[name] = phone
    return f'change {name}: {phone}'


@input_error
def phone(*args):
    name = args[0]
    if name in address_book:
        phone_number = address_book[name]
        return f'phone: {phone_number}'
    return f'Contact not found.'


def show_all():
    return address_book


def parser(text: str) -> tuple[callable, list[str]]:
    if text.startswith('hello'):
        return hello, ()
    
    elif text.startswith('add phone'):
        name, phone = text.replace('add phone', '').strip().split()
        record = Record(name, phone)
        return record.add_phone, (name, phone)
    
    elif text.startswith('add'):
        return add, text.replace('add', '').strip().split()
    
    elif text.startswith('delete phone'):
        name, phone = text.replace('delete phone', '').strip().split()
        record = Record(name, phone)
        return record.delete_phone, (name, phone)
    
    elif text.startswith('edit phone'):
        name, *phone = text.replace('edit phone', '').strip().split()
        record = Record(name, phone)
        return record.edit_phone, (name, phone)
    
    elif text.startswith('change'):
        return change, text.replace('change', '').strip().split()

    elif text.startswith('phone'):
        return phone, text.replace('phone', '').strip().split()
    
    elif text.startswith('show all'):
        return show_all, ()    
    
    return no_comand, ()


def main():
    global address_book
    address_book = AddressBook()
    while True:
        user_input = input('>>>').lower()
        if user_input in ["good bye", "close", "exit"]:
            print('Good bye!')
            break
        command, data = parser(user_input)
        result = command(*data)
        print(result)


if __name__ == '__main__':
    main()
