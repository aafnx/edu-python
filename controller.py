import view

path = './db.txt'

def init():
    create_contact()

def create_contact():
    name = view.get_data('Введите имя: ')
    surname = view.get_data('Введите фамилию: ')
    phone_number = view.get_data('Введите номер телефона: ')
    description = view.get_data('Введите описание: ')
    contact = f'{name};{surname};{phone_number};{description}\n'
    save_data_db(contact)

def save_data_db(data):
    with open(path, 'a') as db:
       db.write(data) 
