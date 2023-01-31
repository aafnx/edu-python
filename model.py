import controller

def add_contact():
    name = controller.get_name()
    surname = controller.get_surname()
    phone_number = controller.get_phone_number()
    description = controller.get_description()
    contact = f'{name};{surname};{phone_number};{description}\n'
    return contact

def change_contact(contact):
    if contact == None:
        return 'Контакт не найден'
    changed_contact = contact.copy()
    controller.view.show(f'Вы изменяетe контакт: {contact}')
    while True:
        command = controller.view.get_data('Какое поле вы хотите изменить (name, surname, phone, desc, q - завершить)?: ')
        match command:
            case 'name':
                changed_contact[0] = controller.get_name()
            case 'surname':
                changed_contact[1] = controller.get_surname()
            case 'phone':
                changed_contact[2] = controller.get_phone_number()
            case 'desc':
                changed_contact[3] = controller.get_description()
            case 'q':
                answer = input(f'Вы подверждаете результат?\n{changed_contact}\n(yes - any key, no - enter no): ')
                if answer.lower() == 'no':
                    return contact
                controller.view.show(f'result - {changed_contact}')
                return changed_contact 
            case _:
                controller.view.show('Введеная неверная команда')
    
    
    
def get_contact(db, name):
    # db = db.split('\n')
    for contact in db:
        for field in contact.split(';'):
            if name.lower() == field.lower():
                return contact.split(';')

def get_all_contacts(db):
    # return db.split('\n')
    return db

