from matplotlib import pyplot as plt
import numpy as np
import math

# define the step size here
step = 0.01

# define the initial point
x0 = 0
y0 = 0.5

# define the end point
end_point = 5.005

# enter the function as seen in y'=f(x,y) to use for 
# Newtons Method.
def f(x,y):
    return y*(y-1)

# this the the function that implement Newtons Method,
# do not change this function.
def system_step(x,y):
    return x+step,y+step*f(x,y)

##### no need to change anything below this line #####

x = [x0]
y = [y0]

number_of_steps = int(math.ceil((end_point-x0)/step))


# note that if additional accuracy is needed, you can format the 
# output below as {0:.8f}, and that will give 8 dicimal points,
# currently it will print 5.
for i in range(0,number_of_steps):
    a, b = system_step(x[i], y[i])
    print("{0:.5f}\t{1:.5f}".format(a, b))
    x.append(a)
    y.append(b)

plt.plot(x,y,label='y(x)')
plt.legend()
plt.show()
