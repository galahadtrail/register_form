"""This module work with sql_lite database"""
import os
import sqlite3
from pathlib import Path

DB_FILENAME = "guests_database.db"


def creating_table():
    basic_query = """
    CREATE TABLE Guests
    ( Id INT, Login STRING, Passwd STRING)
    """
    if not os.path.exists(DB_FILENAME):
        pth = Path(DB_FILENAME)
        pth.touch(exist_ok=True)
    connection = sqlite3.connect(DB_FILENAME)