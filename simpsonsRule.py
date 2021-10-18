# This implements the trapezoidal rule for integration.  
# This method has an error term with an order of 
# magnitude O(h^4).
import math

# define the function to be integrated here
def f(x):
    return math.sin(x)

# define the endpoints of the interval 
a = 0
b = math.pi

# define the number of subintervals, note that for 
# Simpsons Rule, that the number of subintervals must be 
# even.
n = 50

# calculate the step size
h = (b-a)/n

# calculate the values at the end points
endpoints = f(a)+f(b)

twos = 0
fours = 0

for i in range(1,n-2):
    x = a+i*h
    if i%2==0 :
        twos = twos + f(x)
    else :
        fours = fours + f(x)

result = (h/3)*(endpoints+2*twos+4*fours)

print(f"Area: {result}")
