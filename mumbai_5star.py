import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('mumbai_5star.db')

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
    ('Taj  Santacruz', 41800, 22000, 20000),
    ('ITC Maratha', 30250, 16500, 13700),
    ('JW Mariotte', 30000, 15000, 15000),
    ('Trident Nariman Point', 29801, 27240, 14400),
    ('Taj Lands End', 57100, 31100, 28600),
    ('The Westin Garden City', 30000, 13700, 13500),
    ('The Leela', 24000, 14500, 12000),
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
