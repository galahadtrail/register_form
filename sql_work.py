"""This module work with sql_lite database"""
import os
import sqlite3
from pathlib import Path

DB_FILENAME = "guests_database.db"


def creating_table():
    basic_query = """
    CREATE TABLE IF NOT EXISTS Guests
    ( Id integer, Login text, Passwd text)
    """
    if not os.path.exists(DB_FILENAME):
        pth = Path(DB_FILENAME)
        pth.touch(exist_ok=True)
        with sqlite3.connect(DB_FILENAME) as connection:
            connection.executescript(basic_query)


def show_all_data():
    query = "SELECT * FROM Guests"
    with sqlite3.connect(DB_FILENAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
    for data in cursor.fetchall():
        print(data)


def writing_data(u_id: int, name: str, passwd: str):
    search_query = "SELECT * FROM Guests WHERE Id=" + str(u_id)
    query = "INSERT INTO Guests VALUES (?,?,?)"
    with sqlite3.connect(DB_FILENAME) as connection:
        cursor = connection.cursor()
        cursor.execute(search_query)
        if not cursor.fetchone():
            data_cort = (u_id, name, passwd)
            cursor.execute(query, data_cort)
        cursor.close()


def add_new_user(name: str, passwd: str):

    search_query = "SELECT MAX(Id) AS max_id FROM Guests"
    data = False
    with sqlite3.connect(DB_FILENAME) as connection:
        cursor = connection.cursor()
        cursor.execute(search_query)
        data = cursor.fetchone()
        cursor.close()

    if data != (None,):
        print(data)
        u_id = data.Id + 1
    else:
        u_id = 1
    writing_data(u_id, name, passwd)
