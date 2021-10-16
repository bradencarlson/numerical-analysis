import function
# enter iterative function into the function.py file under f(x)

# enter initial guess
x0 = 1.5

# enter tolerance
tol = 0.000001

# enter the maximum number of iterations
N = 500

# do not change anything beneath this line
n = 0

while n<N:
    n = n+1
    x = function.f(x0)
    if abs(x-x0)<tol:
        print(f'fixed point: {x}')
        print(f'iteration count: {n}')
        break
    x0 = x
if n==N:
    print('method failed. max iteration count obtained.')
