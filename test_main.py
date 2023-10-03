"""
Test goes here

"""

#from mylib.calculator import add
from main import main
from main import connect_to_db
from main import create_table
from main import insert_data
from main import read_data
from unittest.mock import patch
import os


def test_main():
    if os.path.exists("test.db"):
        os.remove("test.db")
    conn,cursor = connect_to_db("test.db")
    create_table(cursor)

    insert_data(cursor,"Test User",29)
    data = read_data(cursor)
    assert data == [(1,"Tesr User",29)]

    conn.close()

if __name__ == "__mian__":
    test_main()
    print("PASED")
