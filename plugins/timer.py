from commands.add import run as add
from time import time

def operation_name():
    return "timer"

def run(a, b):
    start = time()
    result = add(a, b)
    end = time()
    print(f"Execution time: {end - start:.6f} seconds")
    return result

