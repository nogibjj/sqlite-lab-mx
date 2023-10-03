"""
ETL-Query script
"""
import sqlite3
import sys
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main():
    try:
         # Extract
        print("Extracting data...")
        file_path = extract()
        print(f"data extraction completed successfully. Saved to {file_path}\n")
       
        # Transform and load
        print("transforming and loading data ...")
        load(file_path)
        print("Data transformation and loading completed successfully.\n")
        
        #query
        print("Querying data...")
        query()
        print("Data querying completed successfully.\n")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def connect_to_db(db_name):
    """
    Connects to a SQLite database and returns the connection and cursor.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn,cursor

def create_table(cursor):
    """
    Creates a table named 'users' if it does not exist.
    cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (
    id INT,
    general_name VARCHAR(255),
    count_products INT,
    ingred_FPro FLOAT,
    avg_FPro_products FLOAT,
    avg_distance_root FLOAT,
    ingred_normalization_term FLOAT,
    semantic_tree_name VARCHAR(255),
    semantic_tree_no INT
    )
    """


def insert_data(cursor,id,general_name):
    cursor.execute(" insert into users (id,general_name) values (?,?) ",(id,general_name))

def read_data(cursor):
    cursor.execute("select * from GroceryDB")
    return cursor.fetchall()

def update_data(cursor,id,general_name):
    cursor.execute("update GroceryDB set general_name = general_name  where id = 6")
    
def delete_data(cursor,id):
    cursor.execute("delete from GroceryDB where id =?",(id,))

if __name__ == "__main__":
    conn,cursor = connect_to_db("GroceryDB.db")
    create_table(cursor)

    #insert_data(cursor, "smith","81","?","?","?","?","?","?","?")
    
    #print("Data after insertions:")
    #print(read_data(cursor))

    update_data(cursor,1,"amy")
    
    print("data after updating amy's name")
    print(read_data(cursor))

    delete_data(cursor,2)

    print("data after deleting amy:")
    print(read_data(cursor))

    conn.commit()
    conn.close()
