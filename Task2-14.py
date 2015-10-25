a=float(input('a = '))
b=float(input('b = '))
import math
fc=1
c_old=0
while fc!=0 :
    c=(a+b)/2
    fa=1/math.tan(1.05*a)-a**2
    fb=1/math.tan(1.05*b)-b**2
    fc=1/math.tan(1.05*c)-c**2
    if c==c_old:
        print(c)
        break
    else:
        if fc*fa==0:
            print('solution ',c)
        elif fa*fc<0:
            c_old=c
            a=a
            b=c
            continue
        elif fb*fc<0:
            c_old=c
            b=b
            a=c
            continue
        else:
            print('wrong')
            break
print(fc)
