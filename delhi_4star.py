import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('delhi_4star.db')

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
    ('Lemon Tree Premier Delhi', 11500, 5940, 5700),
    ('Golden Tulip Vasundhara Hotel and Suites', 7860, 4600, 3880),
    ('Hotel Venus Plaza', 10260, 6300, 5300),
    ('Hotel The Royal Plaza', 14454, 10640, 7200),
    ('ibis Aerocity', 13470, 13400, 6730),
    ('The Hans Hotel', 10200, 5200, 5100),
    ('Hotel Samrat', 13900, 8600, 6910),
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
