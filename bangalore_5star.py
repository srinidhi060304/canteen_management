import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('bangalore_5star.db')

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
    ('The Oberoi', 30000, 29000, 16000),
    ('ITC Gardenia', 38250, 26000, 24000),
    ('Taj Yashwantpur', 17000, 9500, 8500),
    ('Gokulam Grand hotel and spa', 20801, 11040, 10400),
    ('The Park', 17000, 16000, 8500),
    ('Conrad Bangalore', 30000, 11700, 10500),
    ('Leela Bhartiya city', 28000, 14000, 12000),
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
