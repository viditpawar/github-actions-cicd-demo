"""Math utility functions for basic arithmetic operations."""


def add(a, b):
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b (a - b)
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """Divide two numbers.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a and b (a / b)
        
    Raises:
        ValueError: If b (divisor) is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
