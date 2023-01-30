path = './db.txt'

def save(data):
    with open(path, 'a') as db:
        db.write(data)

def read():
    with open(path, 'r') as db:
        return db.read().split('\n')

# def change(contact):
    # with open(path, 'c'):
        
