# implementation of the bisection method

# left end-point
a = 0;

# right end-point 
b = 2;

# define the tolerance
tol = 10^(-6);

# define the function here
function y = f(x)
    y = x^3-0.95;
endfunction

# define the maximum number of iterations
N = 500;

count = 0;

while (b-a)>=2*tol && count < 500
    midpoint = (a+b)/2;
    value = f(midpoint);
    left = f(a);
    right = f(b);
    if value==0
        break;
    elseif left*value <0
        b = midpoint;
    elseif right*value < 0
        a = midpoint;
    endif
    count = count + 1;
endwhile

if count == N
    printf("Max iterations reached.\n");
else
    printf("Zero is approximately %.7f\nerror < %f\n",midpoint,tol);
endif

ans = midpoint;
printf("answer stored in ans\n");



