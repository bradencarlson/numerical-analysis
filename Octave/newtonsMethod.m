
1;

# enter the function here
function y = f(x)
    y = 2*x^2-3*x;
endfunction

# enter the derivative here
function y = fp(x)
    y = 4*x-3;
endfunction

# enter the initial guess here

a = .25;

# define the tolerance
tol = 10^(-12);

# define the maximum number of iterations
N = 500;

count = 0;

while abs(f(a))>=tol && count < N
    diff = f(a)/fp(a);
    a = a- diff;
    count = count +1;
endwhile

if count == N
    fprintf("Maximum number of iterations reached\n")
else
    fprintf("The root is approximately: %.5f\n",a)
endif



