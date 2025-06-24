import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import timer

def test_timer_add():
    assert timer.operation_name() == "timer"
    assert timer.run(5, 2) == 7.0
    assert timer.run(10, -3) == 7.0
