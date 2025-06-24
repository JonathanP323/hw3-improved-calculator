import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import subtract

def test_subtract():
    assert subtract.operation_name() == "subtract"
    assert subtract.run(10, 4) == 6.0
    assert subtract.run(5, 10) == -5.0
    assert subtract.run(0, 0) == 0.0
