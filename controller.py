import view
import model
import db

# commands = ['add', 'find', 'get']

def init():
    request_command()

def request_command():
    while True:
        command = view.get_data('Введите команду (add, find, change, showAll, q): ')

        match command:
            case 'add':
                db.save(model.add_contact())
            case 'find':
                name = get_name()
                view.show(model.get_contact(db.read(), name))
            case 'showAll':
                view.show(model.get_all_contacts(db.read()))
            case 'change':
                name = get_name()
                contact = model.get_contact(db.read(), name)
                changed_contact = model.change_contact(contact)
                db.change(contact, changed_contact)
            case 'q':
                return
            case _:
                view.show('Вы ввели неверную команду')
                
            

def get_name():
    return view.get_data('Введите имя: ')

def get_surname():
    return view.get_data('Введите фамилию: ')

def get_phone_number():
    return view.get_data('Введите номер телефона: ') 

def get_description():
    return view.get_data('Введите описание: ')
