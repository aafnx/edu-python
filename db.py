path_local = './db.txt'
path_export = './db'

def save(data, path = path_local, action = 'a'):
    with open(path, action) as db:
        db.write(data)


def read(path = path_local):
    with open(path, 'r') as db:
        return db.read().split('\n')

def change(contact, changed_contact = None, isdelete = False, path = path_local):
    db = read()
    contact = ';'.join(contact)
    contact_index = db.index(contact)
    if isdelete:
        db[contact_index] = ''
    elif changed_contact == None:
        return 'Error in function change'
    else:
        db[contact_index] = ';'.join(changed_contact)
    db = [item for item in db if item != '']
    data = '\n'.join(db)
    save(data, path, 'w')

def export(format = 'csv', path = path_export):
    data = read()
    data = '\n'.join(data)
    path = f'{path_export}.{format}' 
    save(data, path, 'w')

def import_csv(source_path, path_local = path_local):
    source_db = read(source_path) 
    local_db = read(path_local) 

    data = ''

    for item in source_db:
        if item not in local_db:
            data += f'{item}\n'
    save(data)
