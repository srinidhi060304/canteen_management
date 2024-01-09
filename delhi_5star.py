import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('delhi_5star.db')

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
    ('Shangri La Eros', 28800, 25000, 13000),
    ('Roseate Hotel', 27650, 16280, 11700),
    ('Sheraton New Delhi', 30340, 19000, 10000),
    ('Taj Palace', 1005000, 1003540, 18900),
    ('Maidens Hotel', 40100, 25600, 17600),
    ('The Leela Ambience Convention', 36000, 19500, 18000),
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
