import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('kolkata_sightseeing.db')

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
    ('Victoria Memorial', 'Monument', '5:30am', '6:15pm', 3, 20, 0),
    ('Fort William Kolkata', 'Fort and Monument', '10:00am', '5:30pm', 2, 0, 0),
    ('Balur Math', 'Landmark', '6:30am', '9:00pm', 3, 0, 0),
    ('Birla Planetarium', 'Planetarium', '12:00am', '6:30pm', 3, 40, 40),
    ('Indian Museum', 'Museum', '10:00am', '5:00pm', 2, 10, 10),
    ('Marble Palace Mansion', 'Fort and Palace', '10:00am', '4:00pm', 3, 0, 0),
    ('Mother House', 'Monument', '8:00am', '6:00pm', 2, 0, 0),
    ('Science City Kolkata', 'Museum', '9:00am', '9:00pm', 6, 50, 50),
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
