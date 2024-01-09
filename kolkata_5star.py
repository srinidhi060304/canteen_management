import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('kolkata_5star.db')

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
    ('Hyatt Regency Kolkata', 20000, 11500, 10000),
    ('ITC Royal Bengal', 33550, 28000, 21000),
    ('The Oberoi Grand', 23400, 22500, 11700),
    ('JW Marriott Hotel', 30800, 15140, 15000),
    ('Taj Bengal', 27000, 14000, 12500),
    ('ITC Sonar', 38000, 37000, 19000),
    ('Glenburg The Penthouse', 50900, 49300, 21000),
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
