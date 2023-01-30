import controller

def add_contact():
    name = controller.get_name()
    surname = controller.get_surname()
    phone_number = controller.get_phone_number()
    description = controller.get_description()
    contact = f'{name};{surname};{phone_number};{description}\n'
    return contact

def change_contact(db, name):
    contact = get_contact(db, name)
    if contact == None:
        return 'Контакт не найден'
    controller.view.show(f'Вы изменяетe контакт: {contact}')
    while True:
        command = controller.view.get_data('Какое поле вы хотите изменить (name, surname, phone, desc, q - выход)?: ')
        match command:
            case 'name':
                contact[0] = controller.get_name()
            case 'surname':
                contact[1] = controller.get_surname()
            case 'phone':
                contact[2] = controller.get_phone_number()
            case 'desc':
                contact[3] = controller.get_description()
            case 'q':
                controller.view.show(f'result - {contact}')
                return
            case _:
                controller.view.show('Введеная неверная команда')
    
    
    
def get_contact(db, name):
    for contact in db:
        for field in contact.split(';'):
            if name.lower() == field.lower():
                return contact.split(';')

def get_all_contacts(db):
    return db

