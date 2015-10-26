a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a==0 or b==0 or c==0:
    print ('NSK = 0')
else:
    a1 = a
    b1 = b
    c1 = c
    if a1 / b1 != a1:
        while a1 != b1:
            a1 = a1 + a
            while b1 < a1:
                b1 = b1 + b
    a = a1        
    if a1 / c1 != a1:
        while a1 != c1:
            a1 = a1 + a
            while c1 < a1:
                c1 = c1 + c       

    print ('NSK =', a1)
