"""This module work with sql_lite database"""
import os
import sqlite3

def creating_table():
    basic_query = """
    CREATE TABLE Guests
    ( Id INT, Login STRING, Passwd STRING)
    """