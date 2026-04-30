import numpy as np

def gradient_descent(grad_f, x0, learning_rate, n_steps):
    """
    Performs gradient descent.
    Using 'r' and 'history' internally to match the physics context.
    """
    r = x0
    history = [r]
    
    for _ in range(n_steps):
        # Update using the gradient
        derivative = grad_f(r)
        r = r - learning_rate * derivative
        
        # Append to the history list
        history.append(r)
        
    # Return r as the final result and history as a numpy array
    return r, np.array(history)