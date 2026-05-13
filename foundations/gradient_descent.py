class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        xnew=init
        for i in range (iterations):
            xnew = xnew - learning_rate * 2 * xnew
        return round(xnew, 5)