"""Test suite for math utility functions using pytest."""

import pytest
from src.math import add, subtract, multiply, divide


def test_add():
    """Test addition of two numbers."""
    assert add(2, 3) == 5


def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(5, 3) == 2


def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(4, 5) == 20


def test_divide():
    """Test division of two numbers."""
    assert divide(10, 2) == 5


def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
