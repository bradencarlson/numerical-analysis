import function

a = -0.6675
b = 1.01


tol = 0.00000001
N = 500

n=0

if (b-a)<=0 or function.f(a)*function.f(b)>0:
    print('please enter a valid range for the bisection method.')
else:
    if function.f(a)==0:
        print(f'f({a})=0')
    elif function.f(b)==0:
        print(f'f({b})=0')
    else:
        while n<N:
            n = n+1
            midpoint = (a+b)/2
            if function.f(midpoint)==0:
                print(f'f({midpoint})=0')
                break
            elif function.f(a)*function.f(midpoint)<0:
                b = midpoint
            elif function.f(midpoint)*function.f(b)<0:
                a = midpoint
 
            if (b-a)<tol:
                print(f'f({midpoint})=0\niteration count: {n}')
                break
    if n==N:
        print(f'no solution was found within the iteration limits.')
