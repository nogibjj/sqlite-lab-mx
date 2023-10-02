"""Query the database"""

import sqlite3

#LOG_FILE = "query_log.md"

#def log_query(query):

def query(query):
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    
    cursor = conn.cursor()
    
    cursor.execute(query)
    #"SELECT * FROM GroceryDB"
    if (query.strip().lower().startwith("insert")
        or query.strip().lower().startwith("update")
        or query.strip().lower().startwith("delete"):
            conn.commit()
    cursor.close()
    conn.close()

    #log_query(f"{query}")
    
    #print("Top 5 rows of the GroceryDB table:")
    #print(cursor.fetchall())
#def create():
 #   conn = sqlite3.connect("GroceryDB.db")
  #  c=conn.cursor()
   # c.execute()

def read_data():
    conn=sqlite3.connect("GroceryDB.db")
    c = conn.cursor()
    c.execute("select * from GroceryDB.db limit 5")
    data = c.fetchall()
    return data
