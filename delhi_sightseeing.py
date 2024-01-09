import sqlite3

# Connect to the SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('delhi_sightseeing.db')

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
    ('India Gate', 'Monument', '-', '-', 2, 0, 0),
    ('Qutub Minar', 'Monument', '10:00am', '5:00pm', 3, 40, 0),
    ('Akshardham Temple', 'Temple', '10:00am', '8:00pm', 4, 220, 170),
    ('Humayuns Tumb', 'Monument', '10:00am', '6:00pm', 3, 10, 10),
    ('Museum of Illusions', 'Museum', '11:00am', '9:00pm', 4, 650, 520),
    ('Lotus Temple', 'Temple', '9:15am', '7:00pm', 1, 0, 0),
    ('National Gallery of Modern Art ', 'Art Gallery', '11:00am', '6:30pm', 3, 20, 0),
    ('Red Fort', 'Fort and Pallace', '7:00am', '5:30pm', 3, 10, 0),
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
