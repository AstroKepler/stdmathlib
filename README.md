# stdmathlib

A Python library to simplify mathematical computations.

## Installation

```bash
pip install stdmathlib
```

## Functions

### `integrate_expression`

Integrates a mathematical expression with respect to a variable.

**Parameters:**

- `expression_str` (str): The mathematical expression as a string.
- `var` (str): The variable to integrate with respect to (default is `'x'`).
- `lower_limit` (float, optional): The lower limit of integration.
- `upper_limit` (float, optional): The upper limit of integration.

**Returns:**

- `integral_expr`: The symbolic integral expression (indefinite integral).
- `integral_value` (optional): The numerical value of the definite integral.

**Example Usage:**

```python
from stdmath import integrate_expression

# Indefinite integral
integral_expr = integrate_expression('x**2')
print(f"Indefinite integral: {integral_expr} + C")  # Output: x**3/3 + C

# Definite integral from x=0 to x=2
integral_expr, integral_value = integrate_expression('x**2', lower_limit=0, upper_limit=2)
print(f"Indefinite integral: {integral_expr} + C")          # Output: x**3/3 + C
print(f"Definite integral from 0 to 2: {integral_value}")  # Output: 2.66666666666667
```

### `derivative`

Differentiates a mathematical expression with respect to a variable.

**Parameters:**

- `expression_str` (str): The mathematical expression as a string.
- `var` (str): The variable to differentiate with respect to (default is `'x'`).
- `eval_point` (float, optional): The point at which to evaluate the derivative.

**Returns:**

- `derivative_expr`: The symbolic derivative expression.
- `derivative_value` (optional): The numerical value of the derivative at `eval_point`.

**Example Usage:**

```python
from stdmath import derivative

# Differentiate symbolically
derivative = derivative('x**2 + 3*x + 2')
print(derivative)  # Output: 2*x + 3

# Differentiate and evaluate at x = 2
derivative_expr, derivative_value = derivative('x**2 + 3*x + 2', eval_point=2)
print(derivative_expr)      # Output: 2*x + 3
print(derivative_value)     # Output: 7
```

### `partial_derivative_expression`

Computes the partial derivative of a multivariable function with respect to specified variables.

**Parameters:**

- `expression_str` (str): The multivariable function as a string.
- `variables` (list of str): List of variable names in the function.
- `differentiation_vars` (list of str): List of variables to differentiate with respect to.
- `eval_points` (dict, optional): Dictionary of variable values for evaluation.

**Returns:**

- `derivative_expr`: The symbolic partial derivative expression.
- `derivative_value` (optional): The numerical value of the derivative at `eval_points`.

**Example Usage:**

```python
from stdmath import partial_derivative_expression

# Compute ?f/?x
expression = 'x**2 * y + y**3'
variables = ['x', 'y']
differentiation_vars = ['x']
partial_derivative = partial_derivative_expression(expression, variables, differentiation_vars)
print(partial_derivative)  # Output: 2*x*y
```