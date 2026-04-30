import numpy as np

def f(x):
    """The function to be integrated: 4 / (1 + x^2)."""
    return 4 / (1 + x**2)

def trapezoidal_rule(a, b, n):
    """Approximate the integral of f(x) from a to b using the trapezoidal rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def simpsons_rule(a, b, n):
    """Approximate the integral of f(x) from a to b using Simpson's rule."""
    if n % 2 != 0:
        raise ValueError("n must be an even number")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + 4 * np.sum(y[1::2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

def romberg_integration(a, b, depth):
    """
    Approximates the integral using Romberg Integration (Advanced).
    Each step increases the order of the error cancellation.
    """
    R = np.zeros((depth, depth))
    for i in range(depth):
        R[i, 0] = trapezoidal_rule(a, b, 2**i)
        
        for j in range(1, i + 1):
            factor = 4**j
            R[i, j] = (factor * R[i, j-1] - R[i-1, j-1]) / (factor - 1)
            
    return R[depth-1, depth-1]