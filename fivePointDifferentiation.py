# This implements the five point differentiation method.  It takes in 
# five coordinate points and prints out the approximate values of the
# derivative at all the midopoint, and both the endpoints.
# The five point method has an error term on the order of O(h^4), but 
# the appoximation for the middle point is usually the best.

# enter the x-values of the coordinates here
# note that they must be equally spaced.
x = [1, 2, 3, 4, 5]

# enter the y-values of the coordinates here
y = [1, 4, 9, 16, 25]

# calculate the step size
h = x[1]-x[0]

# calculate the dirivative at the midpoint and at both of the endpoints.

point1 = (1/(12*h))*(-25*y[0]+48*y[1]-36*y[2]+16*y[3]-3*y[4])

point2 = (1/(12*h))*(y[0]-8*y[1]+8*y[3]-y[4])

point3 = (1/(12*h))*(3*y[0]-16*y[1]+36*y[2]-48*y[3]+25*y[4])

print(f"Derivative at {x[0]}: {point1}")
print(f"Derivative at {x[2]}: {point2}")
print(f"Derivative at {x[4]}: {point3}")

