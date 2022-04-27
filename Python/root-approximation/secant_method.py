import function

# enter the function to approximate into the function.py file under f(x)

# enter the initial guess here
x0 = 1.5
x1 = 1.4

# enter the tolerance here
tol = 0.0000001

# enter the max number of iterations
N = 100

# do not change anything below this line
n = 0

while n<N:
    n = n+1
    x2 = x1-function.f(x1)*(x1-x0)/(function.f(x1)-function.f(x0))
    if abs(x2-x1)<tol:
        print(f'f({x2})=0')
        print(f'iteration count: {n}')
        break
    x0 = x1
    x1 = x2
if n==N:
    print(f'max iteration count reached.')
