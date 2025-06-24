import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import add

def test_add():
    assert add.operation_name() == "add"
    assert add.run(5, 3) == 8.0
    assert add.run(-2, 4) == 2.0
    assert add.run(0, 0) == 0.0

