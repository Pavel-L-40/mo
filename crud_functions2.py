import sqlite3



def initiate_db():
    connection = sqlite3.connect('db_crud2.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()
    connection.close()

def add_user(name, email, age, balance = 1000):
    if not is_included(name):
        initiate_db()
        connection = sqlite3.connect('db_crud2.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?,?,?,?)', (name, email,age, balance))
        connection.commit()
        connection.close()
    else:print('this person already here')

def is_included(name):
    connection = sqlite3.connect('db_crud2.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT id FROM Users WHERE username =?', (name,)).fetchone()
    connection.close()
    if check_user:
        return True
    else: return False

def show_users():
    connection = sqlite3.connect('db_crud2.db')
    cursor = connection.cursor()
    list_users = cursor.execute('SELECT * FROM Users')
    message = ''
    for user in list_users:
        message += f'{user[0]} @{user[1]} {user[2]} \n'
    connection.commit()
    return message

# initiate_db()
# print(is_included('first'))
add_user('second', 'exampleer@mail', 23)

