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
from stdmathlib import integrate_expression

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
from stdmathlib import derivative

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
from stdmathlib import partial_derivative_expression

# Compute ?f/?x
expression = 'x**2 * y + y**3'
variables = ['x', 'y']
differentiation_vars = ['x']
partial_derivative = partial_derivative_expression(expression, variables, differentiation_vars)
print(partial_derivative)  # Output: 2*x*y
```

### `plot`

Plots a mathematical expression using `matplotlib`.

**Parameters:**

- `expression_str` (str): The mathematical expression as a string, e.g., `'sin(x)'`.
- `var` (str): The variable in the expression (default is `'x'`).
- `range_start` (float): The start of the range for the variable (default is `-10`).
- `range_end` (float): The end of the range for the variable (default is `10`).
- `num_points` (int): The number of points to compute for plotting (default is `1000`).
- `title` (str): The title of the plot.
- `xlabel` (str): The label for the x-axis.
- `ylabel` (str): The label for the y-axis.
- `line_style` (str): The line style for the plot (e.g., `'-'`, `'--'`, `'-.'`, `':'`).
- `color` (str): The color of the plot line (e.g., `'blue'`, `'red'`, `'#FF5733'`).

**Returns:**

- `None`: Displays the plot.

**Example Usage:**

```python
from stdmathlib import plot
import numpy as np

# Plot y = sin(x) from -2? to 2? with customizations
plot(
    expression_str='sin(x)',
    range_start=-2 * np.pi,
    range_end=2 * np.pi,
    title='Sine Function',
    xlabel='Angle (radians)',
    ylabel='Amplitude',
    line_style='--',
    color='red'
)
```

### `integrate_multivariable_expression`

Computes the multivariable integral of an expression with respect to specified variables.

**Parameters:**

- `expression_str` (str): The mathematical expression as a string.
- `variables` (list of str): List of variable names to integrate with respect to.
- `limits` (list of tuples, optional): List of tuples specifying the limits for each variable.
  Each tuple should be `(variable_name, lower_limit, upper_limit)`.

**Returns:**

- For indefinite integrals: The symbolic integral expression.
- For definite integrals: The numerical value of the integral.

**Example Usage:**

```python
from stdmathlib import integrate_multivariable_expression

# Indefinite integral
integral_expr = integrate_multivariable_expression('x * y', ['x', 'y'])
print(f"Indefinite integral: {integral_expr} + C")

# Definite integral
limits = [('x', 0, 1), ('y', 0, 2)]
integral_value = integrate_multivariable_expression('x * y', ['x', 'y'], limits=limits)
print(f"Definite integral value: {integral_value}")
```

### `factorial`

Computes the factorial of a non-negative integer.

**Parameters:**

- `n` (int): The number to compute the factorial of (n ? 0).

**Returns:**

- `int`: The factorial of `n`.

**Example Usage:**

```python
from stdmathlib import factorial

result = factorial(5)
print(f"5! = {result}")  # Output: 5! = 120
```

### `combinations`

Computes the number combinations of two non-negative integers.

**Parameters:**

- `n` (int): The number of items in the set (n ? 0).
- `r` (int): The number of spots that can be chosen from (n ? r ? 0).

**Returns:**

- `int`: The number of combinations possible given `n` and `r`.

**Example Usage:**

```python
from stdmathlib import combinations

result = combinations(5, 3)
print(f"5C3 = {result}")  # Output: 5C3 = 10
```

### `permutations`

Computes the number of arrangements that `n` can make with the length of `r`, where order is important.

**Parameters:**

- `n` (int): The number of items in the set (n ? 0).
- `r` (int): the number of selected objects arranged in a certain order (n ? r ? 0).

**Returns:**

- `int`: The number of permutations possible given `n` and `r`.

**Example Usage:**

```python
from stdmathlib import permutations

result = permutations(5, 3)
print(f"5P3 = {result}")  # Output: 5P3 = 60
```