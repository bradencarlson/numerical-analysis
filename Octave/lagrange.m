
x = input("Enter an array containing the x-values: ");
y = input("Enter an array containing the y-values: ");

if length(x)!=length(y)
    error("The arrays entered must have the same length");
else

# DO NOT CHANGE
for i=1:length(x)
    product = 1;
    for j = 1:length(x)
        if i!=j
            product = product * (x(i)-x(j));
        endif
    endfor
    product = y(i)/product;
    coeff(i) = product;
endfor

# display the coefficients of the lagrange polynomial 
disp(coeff);

endif
