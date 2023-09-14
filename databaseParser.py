import sqlite3 as sql
import config

db = config.dbName

def makeConnection(db):
    conn = sql.connect(db)
    global cur
    cur = conn.cursor()


def getHomework(request):
    subject, type_of_request = request.split(',')
    cur.execute()
    return f'{type_of_request} {subject}'