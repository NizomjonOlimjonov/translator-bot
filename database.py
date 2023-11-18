import sqlite3
from datetime import datetime

connection  = sqlite3.connect('data1.db')
sql = connection.cursor()

sql.execute("CREATE TABLE if not exists user ( id integer primary key autoincrement ,first_name TEXT, telegram_id integer,phone_number integer, reg_date DATETIME)")
sql.execute("CREATE TABLE if not exists user_word ( id integer primary key autoincrement ,telegram_id integer,text TEXT,translate_text TEXT,added_date DATETIME)")


def register_user(telegram_id,first_name, username):
    commit = sqlite3.connect('database.db')
    cursor = commit.cursor()

    cursor.execute("INSERT INTO user (telegram_id,first_name, username) VALUES (?,?,?)", (telegram_id,first_name,username))

    commit.commit()
    commit.close()








def check_user(user_id):
    commit = sqlite3.connect('database.db')
    cursor = commit.cursor()


    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (user_id,))
    user = cursor.fetchone()

    commit.close()

    if user:
        return True
    else:
        return False


def add_user_word(telegram_id,text,translator_text):
    cursor = sqlite3.connect('database.db')
    cursor = cursor.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS user_words
                      (id INTEGER PRIMARY KEY, user_id INTEGER, word TEXT)''')


    cursor.execute("INSERT INTO user_words (telegram_id,text,translator_text) VALUES (?,?, ?)", (telegram_id,text, translator_text))

   
   
   
   
   
   
   
   
   
    cursor.commit()
    cursor.close()
