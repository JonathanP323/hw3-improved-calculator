"""Unit tests for calculator functions."""

import pytest
from calculator import add, subtract, multiply, divide

from faker import Faker

fake = Faker()

def test_add():
    """Test that the add function returns the correcr sum."""
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    assert add(a, b) == a + b

def test_subtract():
    """Test that the subtract function returns the correct difference."""
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    assert subtract(a, b) == a - b

def test_multiply():
    """Test that the multiply function returns the correct product."""
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    assert multiply(a, b) == a * b

def test_divide():
    """Test that the divide function returns the correct quotient."""
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    assert divide(a, b) == a / b

def test_divide_by_zero():
    """Test dividing by zero raises a ZeroDivisionError."""
    with pytest.raises(ValueError):
        divide(10, 0)

def test_operations(a, b, operation, expected):
    """Test calculator operations using generated data."""
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        pytest.skip("Unknown operation")

    assert result == expected

