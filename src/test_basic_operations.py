# tests/test_basic_operations.py

from src.basic_operations import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
