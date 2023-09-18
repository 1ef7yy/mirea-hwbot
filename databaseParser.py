import sqlite3 as sql
import config


conn = sql.connect(config.dbName)
cur = conn.cursor()

def getHomework(request):
    type_of_request, subject = request.split(',')
    # get_hw = cur.execute(f"SELECT name FROM sqlite_master WHERE name='{subject}'")
    return subject

def addHomework(request):
    type_of_request, subject = request.split(',')
    return 'added ' + subject