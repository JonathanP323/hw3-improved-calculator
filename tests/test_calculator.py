"""Unit tests for calculator functions."""

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test that the add function returns the correcr sum."""
    assert add(2, 3) == 5

def test_subtract():
    """Test that the subtract function returns the correct difference."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Test that the multiply function returns the correct product."""
    assert multiply(4, 3) == 12

def test_divide():
    """Test that the divide function returns the correct quotient."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test dividing by zero raises a ZeroDivisionError."""
    with pytest.raises(ValueError):
        divide(10, 0)
