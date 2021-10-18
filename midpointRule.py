# This implements the trapezoidal rule for integration.  
# This method has an error term with an order of 
# magnitude O(h^2).
import math

# define the function that is to be integrated here
def f(x):
    return math.sin(x)

# define the endopints of the interval for integration
a = 0
b = 5

# define the number of subintervals
n = 500

# calculate the step size
h = (b-a)/n

# calculate the first point
a = a+(1/2)*h

# calculate the area under the curve
total = 0
for i in range(0,n-1):
    total = total + h*f(a+i*h)

# print out the result
print(f"Area: {total}")
