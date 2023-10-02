"""
Test goes here

"""
import subprocess
from mylib.calculator import add


def test_add():
    result = subprocess.run(["python","main.py","extract"],
                           capture_output = True), text = True, check = True,)
    
    assert add(1, 2) == 3

def test_query():
    result = subprocess.run( [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM  WHERE airline = 'Alaska Airlines'",
        ],
        capture_output=True,
        text=True,
        check=True,)
