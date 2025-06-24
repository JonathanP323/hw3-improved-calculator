import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import divide
import pytest

def test_divide():
    assert divide.operation_name() == "divide"
    assert divide.run(20, 5) == 4.0
    assert divide.run(9, 3) == 3.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide.run(10, 0)
