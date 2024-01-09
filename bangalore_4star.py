import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('bangalore_4star.db')

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
    ('Raddison city center', 14500, 9900, 8100),
    ('Howard Johnson', 12000, 6000, 6000),
    ('Royal Orchid Central', 10667, 7055, 5333),
    ('Country Inn and Suites', 9000, 9500, 4500),
    ('Devanam Sarovar Portico', 12000, 7000, 6000),
    ('Kays Select', 12000, 7049, 2299),
    ('Olive Serviced Apartments', 9900, 5200, 4900),
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
