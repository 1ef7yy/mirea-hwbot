import sqlite3 as sql
import config


conn = sql.connect(config.dbName)
cur = conn.cursor()

def getHomework(request: list):
    type_of_request, subject = request
    return f'{type_of_request} {subject}'

def addHomework(request: list):
    type_of_request, subject = request
    return f'{type_of_request} {subject}'