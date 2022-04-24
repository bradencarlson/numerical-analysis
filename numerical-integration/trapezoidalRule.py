# This implements the trapezoidal rule for integration.  
# This method has an error term with an order of 
# magnitude O(h^2).
import math

# define the function that is to be integrated here
def f(x):
    return math.sin(x)

# define the bounds of integration here
a = 0
b = 5

# define the number of subintervals to be used
n = 500

# calculate the step size
h = (b-a)/n

# calculate the area under the curve using the 
# trapezoidal rule
total = f(a)
for i in range(1,n-1):
    total = total + 2*f(a+i*h)

total = total + f(b)
total = (h/2)*total

# print out the results
print(f"Area: {total}")
