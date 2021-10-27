# This implements the three point differentiation method.  It takes in 
# three coordinate points and prints out the approximate values of the
# derivative at all three of those points.  The three point method has 
# an error term on the order of O(h^2), but the appoximation for the 
# middle point is usually the best.

# input the x-values here. Note that for these formulas, the x-values must
# be evenly spaced.
x = [1, 2, 3]

# input the y-values here
y = [1, 4, 9]

# this calculates the step size
h = x[1]-x[0]

point1 = (1/(2*h))*(-3*y[0]+4*y[1]-y[2])

point2 = (1/(2*h))*(y[2]-y[0])

point3 = (1/(2*h))*(y[0]-4*y[1]+3*y[2])

print(f"Derivative at {x[0]}: {point1}")
print(f"Derivative at {x[1]}: {point2}")
print(f"Derivative at {x[2]}: {point3}")


