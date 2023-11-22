"""
This code will import 2 functions from calculus module.
1- def the main fuctions tan(x) and tanh(x)
2-calculate the roots based on the first guess in case of root_simple 
and x0 and x1 for root_bisection
3- calculate accuracy and number of steps
4- make a plot of the roots of tan(x) and tanh(x) using root_simple and root_bisection
"""
import calculus
import matplotlib.pyplot as plt
import re
# Define the functions to be evaluated
def f_tan(x):
    return np.tan(x)
def f_tanh(x):
    return np.tanh(x)
# Define the starting points and x0 and x1 for bisction 
x0_tan_simple = (math.pi /2 + 0.00001)
x0_tan_bisection = (math.pi /2 + 0.00001)
x1_tan_bisection = (3*math.pi /2 - 0.00001)
x0_tanh_simple = -0.5
x0_tanh_bisection = -1
x1_tanh_bisection= 0
# Calculate the roots using root_simple and root_bisection
# for root_debug=True it will print the steps
root_tan_simple, steps_tan_simple = root_simple(f_tan, 
                                                x0_tan_simple, 0.2 , 
                                                accuracy=1.0e-6, 
                                                root_debug=True,
                                                max_steps=1000)
root_tan_bisection, steps_tan_bisection = root_bisection(f_tan,
                                                         x0_tan_bisection,
                                                         x1_tan_bisection,
                                                         accuracy=1.0e-6,
                                                         root_debug=True,
                                                         max_steps=1000)
root_tanh_simple, steps_tanh_simple = root_simple(f_tanh, 
                                                  x0_tanh_simple, 
                                                  0.1, accuracy=1.0e-6, 
                                                  root_debug=True, 
                                                  max_steps=1000)
root_tanh_bisection, steps_tanh_bisection = root_bisection(f_tanh,
                                                           x0_tanh_bisection,
                                                           x1_tanh_bisection,
                                                           accuracy=1.0e-6,
                                                           root_debug=True,
                                                           max_steps=1000)
# Calculate the accuracy
#tan(x)
accuracy_tan_simple = abs(root_tan_simple - 0.0)
accuracy_tan_bisection = abs(root_tan_bisection - 0.0)
#tanh(x)
accuracy_tanh_simple = abs(root_tanh_simple - 0.0)
accuracy_tanh_bisection = abs(root_tanh_bisection - 0.0)
# Print the results for tan(x)
print("----------------Results of tan(x)----------------")
print("---------root_simple---------")
print("Root of tan(x) using root_simple:", root_tan_simple)
print("Accuracy of tan(x) root using root_simple:", accuracy_tan_simple)
print("Steps taken for tan(x) root using root_simple:", len(steps_tan_simple))
print("---------root_bisection---------")
print("Root of tan(x) using root_bisection:", root_tan_bisection)
print("Accuracy of tan(x) root using root_bisection:", accuracy_tan_bisection)
print("Steps taken for tan(x) root using root_bisection:", len(steps_tan_bisection))
# Print the results for tanh(x)
print("----------------Results of tanh(x)----------------")
print("---------root_simple---------")
print("Root of tanh(x) using root_simple:", root_tanh_simple)
print("Accuracy of tanh(x) root using root_simple:", accuracy_tanh_simple)
print("Steps taken for tanh(x) root using root_simple:", len(steps_tanh_simple))
print("---------root_bisection---------")
print("Root of tanh(x) using root_bisection:", root_tanh_bisection)
print("Accuracy of tanh(x) root using root_bisection:", accuracy_tanh_bisection)
print("Steps taken for tanh(x) root using root_bisection:", len(steps_tanh_bisection))
# Plot the functions and their roots
x_vals = np.arange(-5.0, 5.0, 0.01)
y_tan = f_tan(x_vals)
y_tanh = f_tanh(x_vals)
#Plot of the results
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_tan, label='tan(x)')
plt.plot(x_vals, y_tanh, label='tanh(x)')
# plot lines that illustrates the root values
#tan(x)
plt.axvline(x=root_tan_simple, color='red', linestyle='-', label='Root of tan(x) using root_simple')
plt.axvline(x=root_tan_bisection, color='green', linestyle='--', label='Root of tan(x) using root_bisection')
#tanh(x)
plt.axvline(x=root_tanh_simple, color='blue', linestyle='-', label='Root of tanh(x) using root_simple')
plt.axvline(x=root_tanh_bisection, color='yellow', linestyle='--', label='Root of tanh(x) using bisection')
plt.legend()
plt.show()
print("------------------------------digits and Steps________________")
def accuracy_digits(number):
  """Counts the number of digits in a number."""
  number = str(number)
  # If the number starts with a decimal point, add a leading zero.
  if number[0] == ".":
    number = "0" + number
  # If the number ends with an exponent, count the exponent as a significant figure.
  if "e" in number or "E" in number:
    exponent = re.findall(r"[+\-]?\d+", number[-4:])[0]
    number = number[:-4]
  else:
    exponent = 0
  digits = 0
  for char in number:
    if char.isdigit():
      digits += 1
  # Return the number of digits.
  return digits
  
##Tan_accuracy_digits
acc_tan_bisection= accuracy_digits(accuracy_tan_bisection)
acc_tan_simple= accuracy_digits(accuracy_tan_simple)
##Tanh accuracy_digits
acc_tanh_bisection= accuracy_digits(accuracy_tanh_bisection)
acc_tanh_simple= accuracy_digits(accuracy_tanh_simple)
  #results comparing
print("---------for tan(x)---------- \n ","Accuracy \n",
      " the accuracy of root_simple is ", 
      acc_tan_simple , 
      "\n","the accuracy of root_bisection is ", acc_tan_bisection )
print("Steps \n","the number of steps for root_simple is ",
      len(steps_tan_simple), "\n",
      "the number of steps for the root_bisection is",
      len(steps_tan_bisection))
print("---------for tan(x)---------- \n ","Accuracy \n", 
      " the accuracy of root_simple is ",
      acc_tanh_simple , "\n","the accuracy of root_bisection is ",
      acc_tanh_bisection  )
print("Steps \n","the number of steps for root_simple is ",
      len(steps_tanh_simple), "\n",
      "the number of steps for the root_bisection is",
      len(steps_tanh_bisection))
