import sqlite3
if __name__ == '__main__':
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        age INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    print('Users table created.')
    username = str(input('Enter username: '))
    age = int(input('Enter age: '))
    cursor.execute('''
    INSERT INTO users (username, age)
        VALUES (?, ?)
        ''', (username, age))
    db.commit()

    printdb = str(input('Do u want to print db ? (Y)es/No: '))
    printdb = printdb.lower()

    if printdb == 'y' or printdb == 'yes' or printdb == "":
        print("U selected yes")

        data = cursor.execute('''SELECT * FROM users''')
        for row in data:
            print(row)

    else:
        print("U selected no")
