import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('kolkata_4star.db')

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
    ('Kenilworth Hotel', 18800, 14100, 9500),
    ('Polo Floatel', 10320, 9200, 5500),
    ('Hotel De Sovrani', 8767, 5155, 4233),
    ('The Peerless Hotel', 13400, 8300, 7500),
    ('The Elgin FairLawn', 19200, 12400, 9300),
    ('Holiday Inn', 14200, 7449, 7129),
    ('Howard Johnson', 10800, 7800, 5900),
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
