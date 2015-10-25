from math import exp
eps=float(input('eps='))
a=1
b=2
while abs(a-b)>eps:
    c=(a+b)/2
    k=(exp(-c)+c**2-2)*(exp(-a)+a**2-2)
    if k<0:
        b=c
    else:
        a=c
    print(a,b)
if a==b:
    print('x=',c)
else:
    print('приблизне значення кореня =',c)    
