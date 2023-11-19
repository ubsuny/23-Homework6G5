from calculus import simpson, trapeziod, adaptive_trapezoid
import numpy as np
import matplotlib.pyplot as plt

# def exp(x):
#     # To handle the singularity at x = 0
#     return np.where(x != 0, np.exp(-1/x), 0)

# def cos(x):
#     # To handle the singularity at x = 0
#     return np.where(x !=0, np.cos(1/x),0)

# However, there is still a RuntimeWarning that encountred  due to the behavior
# of the functions exp and cos near zero. These functions have singularities or
# behave erratically as x approaches zero. We can resolve this issue by modifying
# functions:
def exp(x):
    # Using np.exp safely with np.clip to avoid overflow
    safe_x = np.clip(x, 1e-10, np.inf) #np.clip is used to limit the values of x
                                      # to a range that avoids division by zero
                                      # and overflow issues. It effectively replaces
                                      # very small values (close to zero) with a small
                                      # but non-zero number (1e-10 in this case).
    return np.where(x != 0, np.exp(-1/safe_x), 0)

def cos(x):
    # Limiting the input to cos to avoid invalid values
    safe_x = np.clip(x, 1e-10, np.inf)
    return np.where(x != 0, np.cos(1/safe_x), 1)


def cubic(x, constant=1/2):
    return x**3 + constant
