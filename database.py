#Version 1.2

import sqlite3, time

file = "sensors.db"
try:
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    
    cmd = "CREATE TABLE Sensors(Datum var_char(255), Zeit var_char(255), eco2 int,  tvoc int, humidity int, temperature int, Primary Key (datum, zeit))"
    #cursor.execute(cmd)
    
    # Queries to INSERT records.
    currenttime = time.strftime("%H:%M:%S", time.localtime())
    currentdate = time.strftime("%d.%m.%Y", time.localtime())
    
    insertQuery = "INSERT INTO SENSORS VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(insertQuery, (currentdate, currenttime, 800, 3, 16, 14))
    
    # Commit your changes in the database    
    conn.commit()
    
    # Display columns
    print('\nColumns in Sensors table:')
    data=cursor.execute("SELECT * FROM Sensors")
    for column in data.description:
        print(column[0])   
        
    # Display data
    print('\nData in Sensors table:')
    data=cursor.execute("SELECT * FROM Sensors")
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