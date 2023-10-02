"""
Test goes here

"""
import subprocess
from mylib.calculator import add


def test_add():
    result = subprocess.run(["python","main.py","extract"],
                           capture_output = True), text = True, check = True,)
    
    assert add(1, 2) == 3

def test_query(): #add where condition
    result = subprocess.run( [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM GroceryDB.db ,
        ],
        capture_output=True,
        text=True,
        check=True,)
   assert add(1, 2) == 3

def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert add(1,2) == 3
if __name__ =="__main__":
    test_add()
    test_read_data()
    test_query()
