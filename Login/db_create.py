import sqlite3

# Connect to the database
connection = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE students (
        username TEXT PRIMARY KEY,
        email TEXT,
        password TEXT,
        no_of_projects INTEGER,
        xp INTEGER  
    )
''')

# # Commit the changes
connection.commit()

# # Insert data
# cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", ('john_doe', 'john@example.com', 'password123'))
# cursor.execute('''
#     CREATE TABLE mentor (
#         id INTEGER PRIMARY KEY,
#         username TEXT,
#         email TEXT,
#         password TEXT
#     )
# ''')
# connection.commit()

# # Close the database
connection.close()
