"""This module work with sql_lite database"""
import os
import sqlite3
from pathlib import Path

DB_FILENAME = "guests_database.db"


def creating_table():
    basic_query = """
    CREATE TABLE IF NOT EXIST SGuests
    ( Id integer, Login text, Passwd text)
    """
    if not os.path.exists(DB_FILENAME):
        pth = Path(DB_FILENAME)
        pth.touch(exist_ok=True)
        with sqlite3.connect(DB_FILENAME) as connection:
            connection.executescript(basic_query)


def add_new_user(name: str, passwd: str):
    query = "INSERT INTO Guests VALUES (?,?,?)"
    search_query = "SELECT MAX(Id) FROM AS max_id guests_database.db"
    data = False
    with sqlite3.connect(DB_FILENAME) as connection:
        cursor = connection.cursor()
        cursor.execute(search_query)
        data = cursor.fetchone()
        cursor.close()

    if data:
        u_id = data + 1
        with sqlite3.connect(DB_FILENAME) as connection:
            cursor = connection.cursor()
            data_cort = (u_id, name, passwd)
            cursor.execute(query, data_cort)
            cursor.close()