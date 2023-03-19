import sqlite3

DB_NAME = '/Users/Nikhil/Documents/FSNotes/API/notes.db'

def getNotes():

    connection = None

    try:
        connection = sqlite3.connect(DB_NAME)
    except:
        return "ERROR: Failed to connect to database"

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes')

    data = cursor.fetchall()
    connection.commit()
    connection.close()

    retVal = []

    for string in data:
        retVal.append(string[0])

    return str(retVal).replace('\'','\"')

def addNote(note):

    decodedNote = note.decode('utf-8')
    decodedNote = decodedNote[1:len(decodedNote)-1]

    connection = None
    
    try:
        connection = sqlite3.connect(DB_NAME)
    except:
        return "ERROR: Failed to connect to database"

    cursor = connection.cursor()
    cursor.execute('INSERT INTO notes VALUES (?)', (decodedNote,))
    connection.commit()
    connection.close()

    return note

def deleteNote(id):

    connection = None

    try:
        connection = sqlite3.connect(DB_NAME)
    except:
        return "ERROR: Failed to connect to database"

    cursor = connection.cursor()
    cursor.execute('DELETE FROM Notes WHERE ROWID = (?)', (int(id) + 1,))
    connection.commit()
    connection.close()

    return id