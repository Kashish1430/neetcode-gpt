class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return init
        # At each Iteration
        # We compute x = x - learning_rate * f'(x); where f'(x) = 2x
        x_old = init # 5
        x_new = None
        for i in range(iterations):
            #derivate = get_derivative(x_old)
            x_new = x_old - learning_rate * (x_old * 2)
            x_old = x_new
            
        return round(x_new, 5)
