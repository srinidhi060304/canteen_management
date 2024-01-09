import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('bangalore_sightseeing.db')

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
    ('Lalbagh', 'Garden and Park', '6:00am', '7:00pm', 3, 25, 0),
    ('Church Street', 'Shopping Market', '-', '-', 5, 0, 0),
    ('Bannerghatta National Park', 'National Park', '9:30am', '5:00pm', 6, 80, 40),
    ('Bangalore Palace', 'Fort and Palace', '10:00am', '5:30pm', 4, 230, 230),
    ('Cubbon Park', 'Garden and Park', '6:00am', '6:00pm', 2, 0, 0),
    ('ISKCON Temple', 'Temple', '7:15am', '8:30pm', 3, 0, 0),
    ('Wonderla Amusment Park', 'Amusment and Theme Park', '11:00am', '7:00pm', 7, 1349, 1349),
    ('Innovation Film City', 'Amusment and Theme Park', '10:00am', '7:00pm', 5, 600, 600),
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
