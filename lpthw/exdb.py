import sqlite3

trajetstrains2 = sqlite3.connect('exdb.db')

sqlite3.Cursor.execute('''CREATE TABLE Trains(
                code CHAR(5) PRIMARY KEY NOT NULL, 
                codetrain INT
                )
              ''')
