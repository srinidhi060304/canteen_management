import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('mumbai_3star.db')

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
    ('Hotel Pacific Residency', 12100, 7900, 5500),
    ('Hotel Wego', 10350, 10400, 5300),
    ('Keys Select by Lemon Tree', 9370, 5200, 4600),
    ('Sea Green South Hotel', 12550, 9040, 7500),
    ('Hotel Metro Palace', 8770, 5200, 4230),
    ('Theory9', 13200, 8200, 7900),
    ('Hotel Airport International', 13900, 8380, 7400),
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
