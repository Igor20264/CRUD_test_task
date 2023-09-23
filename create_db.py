import sqlite3

def create_db(name):

    conn = sqlite3.connect(b'database.db',check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Booking (
    id INTEGER UNIQUE PRIMARY KEY ASC AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    start_time INTEGER NOT NULL,
    end_time INTEGER NOT NULL,
    comment TEXT
    )
    ''')
                
    cursor.execute('''
    CREATE TABLE User (
        id INTEGER UNIQUE PRIMARY KEY ASC AUTOINCREMENT, 
        username TEXT (255) NOT NULL, 
        password TEXT (1024) NOT NULL, 
        created INTEGER NOT NULL, 
        updated INTEGER NOT NULL)
    ''')
                
    conn.commit()

    return conn