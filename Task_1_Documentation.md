# Documentation for Task one.
## Main objectives
### 1. Implementation of Integral Algorithms
To develop a Jupyter notebook that incorporates integral algorithms (Simpson, Adaptive Trapezoid, Trapezoid) from the `calculus.py` module. These algorithms will be utilized to compute and visualize the definite integral of a given function over different specified boundaries.
### 2. Accuracy and Efficiency Comparison
To compare the accuracy of each algorithm by evaluating how many correct digits they provide for the integral result. Additionally, assess the efficiency of the algorithms by determining the number of steps required to achieve a given level of accuracy.

## Introduction to Integral Algorithms:
### Simpson's Rule
**Simpson's Rule** is a numerical integration method that approximates the definite integral of a function by using quadratic polynomials to approximate small sections of the curve. Named after the mathematician Thomas Simpson, this technique provides a more accurate result than simpler methods like the trapezoidal rule, especially when dealing with functions that exhibit curvature.
The fundamental idea behind Simpson's Rule is to divide the area under the curve into small intervals and approximate each interval with a quadratic polynomial. The formula for Simpson's Rule can be expressed as follows:

The integral of f(x) from a to b, approximated by Simpson's Rule:

    h
    - [f(x₀) + 4f(x₁) + f(x₂)]
    3

Simpson's Rule provides a more accurate estimate of the integral by considering the curvature of the function within each interval. It is particularly useful for functions that can be well approximated by quadratic polynomials. As the number of intervals increases, Simpson's Rule tends to converge to the exact value of the integral.

### Trapezoid Rule:
**Trapezoid Rule** is a numerical integration method used to approximate the definite integral of a function by dividing the area under the curve into trapezoids. This method is a straightforward and intuitive approach for estimating integrals, especially when the analytical solution is challenging to obtain.
The formula for the Trapezoid Rule is given by:

   The integral of f(x) from a to b, approximated by the Trapezoid Rule:

    h
    - [f(x₀) + 2f(x₁) + ... + 2f(xₙ₋₁) + f(xₙ)]
    2

Here:
- h is the width of each subinterval (h = (b - a) / n),
- n is the number of subintervals,
- x₀, x₁, ..., xₙ are the points defining the subintervals.

The Trapezoid Rule assumes that the function is piecewise linear within each subinterval, connecting the points on the curve with straight lines to form trapezoids. While it may not be as accurate as more sophisticated methods for certain functions, the Trapezoid Rule is computationally simple and can provide reasonably accurate results for well-behaved functions.

In applications where precision is less critical or when dealing with functions where the curvature is not extreme, the Trapezoid Rule serves as a reliable method for numerical integration.
### Adaptive Trapezoid Rule:

**Adaptive Trapezoid Rule** is an enhancement of the traditional Trapezoid Rule, designed to improve accuracy by dynamically adjusting the number of subintervals based on the behavior of the function. This adaptive approach allows the algorithm to focus computational effort where the function is more complex or rapidly changing, providing a more accurate estimation of the definite integral.
The formula for the Adaptive Trapezoid Rule involves recursively applying the Trapezoid Rule on subintervals until a specified level of accuracy is achieved. The process involves iteratively refining the approximation until the difference between successive estimates falls below a predetermined tolerance.
The Adaptive Trapezoid Rule can be summarized as follows:

1. Divide the interval [a, b] into two subintervals.
2. Apply the Trapezoid Rule on each subinterval.
3. Sum the results from step 2 to obtain an initial approximation.
4. Check if the difference between the initial approximation and the sum of the Trapezoid Rule applied to the individual subintervals is below the specified tolerance.
5. If the tolerance is met, return the current approximation; otherwise, recursively apply steps 1-4 on each subinterval.

The Adaptive Trapezoid Rule provides a balance between accuracy and efficiency, adapting the resolution of the integration based on the local behavior of the function. This makes it particularly useful for functions with varying levels of complexity across different regions.

In practical applications, the Adaptive Trapezoid Rule is advantageous when dealing with functions that may have rapidly changing behavior in some regions while being relatively smooth in others.
## Defining the three integral method in the module Calculus.py
```python
import numpy as np

def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite Simpson's rule, using n subintervals.
    
    Parameters:
    - f (function): The integrand function.
    - a (float): The lower limit of integration.
    - b (float): The upper limit of integration.
    - n (int): The number of subintervals.

    Returns:
    float: Approximation of the definite integral using Simpson's rule.
    """
    h = (b - a) / n
    i = np.arange(0, n)

    s = f(a) + f(b)
    s += 4 * np.sum(f(a + i[1::2] * h))
    s += 2 * np.sum(f(a + i[2:-1:2] * h))

    return s * h / 3

def trapezoid(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals.
    
    Parameters:
    - f (function): The integrand function.
    - a (float): The lower limit of integration.
    - b (float): The upper limit of integration.
    - n (int): The number of subintervals.

    Returns:
    float: Approximation of the definite integral using the trapezoidal rule.
    """
    h = (b - a) / n
    s = f(a) + f(b)
    i = np.arange(0, n)
    s += 2 * np.sum(f(a + i[1:] * h))
    return s * h / 2

def adaptive_trapezoid(f, a, b, acc, output=False):
    """
    Uses the adaptive trapezoidal method to compute the definite integral
    of f from a to b to desired accuracy acc.
    
    Parameters:
    - f (function): The integrand function.
    - a (float): The lower limit of integration.
    - b (float): The upper limit of integration.
    - acc (float): The desired accuracy.
    - output (bool): If True, print the iteration information.

    Returns:
    float: Approximation of the definite integral using adaptive trapezoidal rule.
    """
    old_s = np.inf
    h = b - a
    n = 1
    s = (f(a) + f(b)) * 0.5
    if output:
        print("N = " + str(n + 1) + ",  Integral = " + str(h * s))
    while abs(h * (old_s - s * 0.5)) > acc:
        old_s = s
        for i in np.arange(n):
            s += f(a + (i + 0.5) * h)
        n *= 2.
        h *= 0.5
        if output:
            print("N = " + str(n) + ",  Integral = " + str(h * s))
    return h * s
```


## Using the Three Integral Methods in Exponential Function exp(-1/x):

The boundary conditions used for the exponential is [0, 10*5], as our group number is 5. Using this boundary condition, we will get singularity at x=0, so to remove this error, we have to use small value rather than zero in the boundary condition. I have used it as follows:
``` python
# Define the function exp(-1/x)
def exp_func(x):
    # Avoid zero
    epsilon = 1e-10
    return np.where(np.abs(x) < epsilon, np.nan, np.exp(-1 / x))
```
In next step, we defined the number of intervals and bounds.
```python
a_exp = 1e-10
b_exp = 50
n_exp = 10
```
 In this section, we calculate and print results for the definite integral of the function using three different numerical integration methods: the Trapezoidal Rule, Simpson's Rule, and the Adaptive Trapezoidal Rule.
 ```python
# Calculate and print results using the trapezoidal rule
ans_exp_trapezoid = trapezoid(exp_func, a_exp, b_exp, n_exp)
print('Trapezoidal rule result for exp(-1/x):', ans_exp_trapezoid)

# Calculate and print results using Simpson's rule
ans_exp_simpson = simpson(exp_func, a_exp, b_exp, n_exp)
print('Simpson\'s rule result for exp(-1/x):', ans_exp_simpson)

# Calculate and print the result using the adaptive trapezoidal rule for exp(-1/x)
ans_adaptive_trapezoid_exp = adaptive_trapezoid(exp_func, a_exp, b_exp, 0.0001, output=True)
print('Adaptive trapezoidal rule result for exp(-1/x):', ans_adaptive_trapezoid_exp)
```
The integration values from each methods is listed below:
```python

Trapezoidal rule result for exp(-1/x): 44.767875582331264
Simpson's rule result for exp(-1/x): 45.394860137465905
N = 2,  Integral = 24.50496683261987
N = 2.0,  Integral = 36.2722193950719
N = 4.0,  Integral = 41.84613589424154
N = 8.0,  Integral = 44.33629552340518
N = 16.0,  Integral = 45.32211379318896
N = 32.0,  Integral = 45.62074101600314
N = 64.0,  Integral = 45.66332231905843
N = 128.0,  Integral = 45.656444665639235
N = 256.0,  Integral = 45.65514251840915
N = 512.0,  Integral = 45.6552280711973
Adaptive trapezoidal rule result for exp(-1/x): 45.6552280711973
```


