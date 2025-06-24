import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import multiply

def test_multiply():
    assert multiply.operation_name() == "multiply"
    assert multiply.run(6, 7) == 42.0
    assert multiply.run(0, 5) == 0.0
    assert multiply.run(-3, 2) == -6.0
