import pytest
from faker import Faker 

fake = Faker()

def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=1, type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        num = metafunc.config.getoption("num_records")
        records = []

        for _ in range(num):
            a = fake.random_int(min=1, max=100)
            b = fake.random_int(min=1, max=100)
            operation = fake.random_element(elements=("add", "subtract", "multiply", "divide"))
            if operation == "add":
                expected = a + b
            elif operation == "subtract":
                expected = a - b
            elif operation == "multiply":
                expected = a * b
            elif operation == "divide":
                expected = a / b
            records.append((a, b, operation, expected))

        metafunc.parametrize("a,b,operation,expected", records)
