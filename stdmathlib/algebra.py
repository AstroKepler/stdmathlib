# stdmath/algebra.py

def solve_linear(a, b):
    """Solve a linear equation ax + b = 0."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    return -b / a

def quadratic_formula(a, b, c):
    """Solve a quadratic equation ax^2 + bx + c = 0."""
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real roots.")
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2
