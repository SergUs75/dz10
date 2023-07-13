from collections import UserDict


class Field:
    pass
    

class Name(Field):
    def __init__(self, name):
        self.name = name
    def __str__(self):
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
    
    def add_phone_record(self, phone):
        self.phones.append(phone)

    def delete_phone_record(self, phone):
        self.phones.remove(phone)

    def edit_phone_record(self, old_phone, new_phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)


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


@input_error
def add_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.name in address_book:
        record = address_book[name.name]
        record.add_phone_record(phone)
        return f'Add {name}: {phone}'
    

@input_error
def delete_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.name in address_book:
        record = address_book[name.name]
        for p in record.phones:
            if p.phone == phone.phone:
                record.delete_phone_record(p)
                return f'Deleted {phone} from {name}'


@input_error
def edit_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    if name.name in address_book:
        record = address_book[name.name]
        for p in record.phones:
            if p.phone == old_phone.phone:
                record.edit_phone_record(p, new_phone)
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
        return add_phone, text.replace('add phone', '').strip().split()
    
    elif text.startswith('add'):
        return add, text.replace('add', '').strip().split()
    
    elif text.startswith('delete phone'):
        return delete_phone, text.replace('delete phone', '').strip().split()
    
    elif text.startswith('edit phone'):
        return edit_phone, text.replace('edit phone', '').strip().split()
    
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
