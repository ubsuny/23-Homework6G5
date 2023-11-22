# Root Finding
## functions based on calculus module:
The root_simple algorithm is a simple step-halving algorithm that starts with an initial guess and a step size. It then iteratively halves the step size and moves towards the root until it reaches the desired accuracy.
The root_bisection algorithm is a bracketing algorithm that starts with two points that are known to bracket the root. It then iteratively bisects the interval between the two points until it reaches the desired accuracy.
The root_secant algorithm is a more sophisticated algorithm that uses the secant line to estimate the root. It starts with two initial guesses and then iteratively updates the guesses based on the secant line.
The root_tangent algorithm is a derivative-based algorithm that uses the tangent line to estimate the root. It starts with an initial guess and then iteratively updates the guess based on the tangent line.
All four of the algorithms are implemented in Python and can be used to find the roots of any function. The algorithms are all well-documented and easy to use.
**the functions we worked on are root_simple and root_bisection**

## Functions we studied:
Tan(x):
A struggle with tan(x) function is to aviod being stuck at a minima. From the illustration below the code may give the root of tan(x) at x= $\pi/2$
we tried to avoid this by creating x0 and x1 as ${\pi/2 + 0.0001}$ and ${3\pi/2 -0.0001}$
fig.(1) Roots of Tan(x) [Wolframe](https://mathworld.wolfram.com/Tangent.html)
<img width="308" alt="Screen Shot 2023-11-22 at 2 51 33 PM" src="https://github.com/yasmensarhan27/23-Homework6G5/assets/38404107/1c91b130-3b53-4295-81c6-fdaeac00a724"> 



Tanh(x)
For Tanh(x), the only root it has is 0 but for the root_functions to iterate and reach the required accuracy we didn't start or make the initial guess as zero but -1 
Fig.(2) Roots of Tanh(x) [Wikipedia](https://en.wikipedia.org/wiki/Hyperbolic_functions)
![Tanh(x)](https://github.com/yasmensarhan27/23-Homework6G5/assets/38404107/24842bb0-1e0c-4131-b385-5669091baa11) 


**The results we got**:

![Unknown-9](https://github.com/yasmensarhan27/23-Homework6G5/assets/38404107/600c1266-5ea8-47c6-b756-88fad73082c4)


According to the functions we used for measuring the roots the values were 

```
------Tan(x)-------
---------root_simple---------
Root of tan(x) using root_simple: 3.1415918492558355
Accuracy of tan(x) root using root_simple: 3.1415918492558355
Steps taken for tan(x) root using root_simple: 36
---------root_bisection---------
Root of tan(x) using root_bisection: 3.1415930280944373
Accuracy of tan(x) root using root_bisection: 3.1415930280944373
Steps taken for tan(x) root using root_bisection: 23
Accuracy
  the accuracy of root_simple is  17 
 the accuracy of root_bisection is  17
Steps
 the number of steps for root_simple is  36 
 the number of steps for the root_bisection is 23
```

```
----------------Results of tanh(x)----------------
---------root_simple---------
Root of tanh(x) using root_simple: -2.7755575615628914e-17
Accuracy of tanh(x) root using root_simple: 2.7755575615628914e-17
Steps taken for tanh(x) root using root_simple: 23
---------root_bisection---------
Root of tanh(x) using root_bisection: -4.76837158203125e-07
Accuracy of tanh(x) root using root_bisection: 4.76837158203125e-07
Steps taken for tanh(x) root using root_bisection: 21

---------for tanh(x)---------- 
  Accuracy 
  the accuracy of root_simple is  17 
 the accuracy of root_bisection is  15
Steps 
 the number of steps for root_simple is  23 
 the number of steps for the root_bisection is 21

```
## steps of the code
 The code first imports the necessary libraries, including the calculus module, matplotlib.pyplot, and re.
 
 Then, it defines two functions to be evaluated: f_tan(x) and f_tanh(x). These functions return the tangent and hyperbolic tangent of x, respectively.
 
Next, the code defines the starting points for the root_simple and root_bisection algorithms. The starting points for the root_simple algorithm are x0_tan_simple = (math.pi /2 + 0.00001) and x0_tanh_simple = -0.5.
The starting points for the root_bisection algorithm are x0_tan_bisection = (math.pi /2 + 0.00001) and x1_tan_bisection = (3*math.pi /2 - 0.00001) for tan(x), and x0_tanh_bisection = -1 and x1_tanh_bisection = 0 for tanh(x).

The code then calculates the roots of the functions using the root_simple and root_bisection algorithms. The root_simple algorithm takes a function, a starting point, a step size, and an accuracy as input.
The root_bisection algorithm takes a function, two starting points, and an accuracy as input. Both algorithms return the root of the function and the number of steps taken to find it.

The code then calculates the accuracy of the roots using the following formula: accuracy = abs(root - 0.0). The accuracy is a measure of how close the root is to the true value.

Finally, the code plots the functions and their roots using matplotlib.pyplot. The plot shows the functions and their roots, as well as lines that illustrate the root values.

The code is well-written and easy to understand. It is also well-commented, which makes it easy to follow. The code is also efficient and runs quickly.
