import sqlite3

connection = sqlite3.connect('database.db')

with connection:
    connection.execute('''
        CREATE TABLE evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL,
            evaluation INTEGER NOT NULL,
            comments TEXT NOT NULL
        );
    ''')

connection.close()