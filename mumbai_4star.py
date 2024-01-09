import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('mumbai_4star.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with columns: hotel_name, 4people, 3people, 2people
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotels (
        hotel_name TEXT PRIMARY KEY,
        fourpeople INTEGER,
        threepeople INTEGER,
        twopeople INTEGER
    )
''')

# Save (commit) the changes
conn.commit()

# Insert data into the table
hotel_data = [
    ('Lemon Tree', 14800, 13000, 7100),
    ('Raddison,Goregaon', 18350, 10500, 9700),
    ('IRA by Orchid', 16260, 9000, 7500),
    ('Mirrage Hotel', 16454, 10540, 8200),
    ('Ramee Guestline Hotel', 19470, 10700, 9730),
    ('Dragonfy Art Hotel', 15300, 8700, 7600),
    ('The Empresa', 20100, 11600, 10000),
    # Add more hotels as needed
]

# Use executemany to insert multiple rows at once
cursor.executemany('''
    INSERT OR REPLACE INTO hotels (hotel_name, fourpeople, threepeople, twopeople)
    VALUES (?, ?, ?, ?)
''', hotel_data)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
