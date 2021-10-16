import function

# enter initial guess
x0 = 1.5

# enter tolerance
tol = 0.00001

# enter maximum number of iterations
N = 100

# do not change anything beneath this line
n = 0

while n<N:
    n = n+1
    x = x0-function.f(x0)/function.f_prime(x0)
    if abs(x-x0)<tol:
        print(f'f({x})=0')
        print(f'iteration count: {n}')
        break
    x0 = x
if n==N:
    print(f'max iteration count reached.')
