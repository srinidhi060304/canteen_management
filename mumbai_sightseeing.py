import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('mumbai_sightseeing.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with columns: hotel_name, 4people, 3people, 2people
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sightseeing (
        name TEXT PRIMARY KEY,
        tag TEXT,
        starttime TEXT,
        endtime TEXT,
        timerequired INTEGER,
        adultentry INTEGER,
        childentry INTEGER
    )
''')

# Save (commit) the changes
conn.commit()

# Insert data into the table
sightseeing_data = [
    ('Elephanta Caves', 'Caves', '9:00am', '5:30pm', 5, 10, 0),
    ('Marine Drive', 'Beach', '-', '-', 2, 0, 0),
    ('Colaba Causeway', 'Commercial Street', '-', '-', 3, 0, 0),
    ('Juhu Beach', 'Beach', '-', '-', 2, 0, 0),
    ('Gateway of India', 'Monument', '-', '-', 2, 0, 0),
    ('Prince of Wales Museum', 'Museum', '10:15am', '5:00pm', 5, 30, 30),
    ('Essel World', 'Amusment and Theme Park', '10:00am', '7:00pm', 7, 1050, 1050),
    ('Film City Mumbai', 'Amusment and Theme Park', '10:00am', '5:00pm', 4, 800, 800),
    # Add more hotels as needed
]

# Use executemany to insert multiple rows at once
cursor.executemany('''
    INSERT OR REPLACE INTO sightseeing (name ,tag ,starttime ,endtime ,timerequired ,adultentry ,childentry)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', sightseeing_data)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
