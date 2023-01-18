import sqlite3, datetime

file = "sensors.db"
try:
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    date = datetime.datetime.now()
    
    cursor.execute("Drop database sensors.py")
    
    cmd = "CREATE TABLE Sensors(datum var_char(255), eco2 int,  tvoc int, humidity int, temperature int)"
    cursor.execute(cmd)
    
    # Queries to INSERT records.
    cmd1 = "INSERT INTO Sensors(eco2, tvoc, humidity, temperature) VALUES (" + str(date) + ", 400, 0, 5, 21)"
    cursor.execute(cmd1)
    
    # Commit your changes in the database    
    conn.commit()
    
    # Display columns
    print('\nColumns in Sensors table:')
    data=cursor.execute('''SELECT * FROM Sensors''')
    for column in data.description:
        print(column[0])   
        
    # Display data
    print('\nData in Sensors table:')
    data=cursor.execute('''SELECT * FROM Sensors''')
    for row in data:
        print(row) 
    
    # Commit your changes in the database    
    conn.commit()
    
    
except sqlite3.Error as error:
    print("Failure", error)
    
finally:
    if conn:
        conn.close()
        print("Closed")