import os
import sqlite3
from sqlite3 import Error

def connect():
    try:
        con = sqlite3.connect('db.sqlite3')
        return con

    except Error:
        print(Error)

def init(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS prices(price text, date text)")
    con.commit()


def insert(con, price):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO prices(price, date) VALUES(?, ?)', price)
    con.commit()

def fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM prices')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)
