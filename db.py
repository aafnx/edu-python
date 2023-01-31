path = './db.txt'

def save(data):
    with open(path, 'a') as db:
        db.write(data)

def read():
    with open(path, 'r') as db:
        return db.read().split('\n')

def change(contact, changed_contact):
    db = read()
    contact = ';'.join(contact)
    contact_index = db.index(contact)
    db[contact_index] = ';'.join(changed_contact)
    data = '\n'.join(db)
        
    with open(path, 'w') as db:
        db.write(data)
