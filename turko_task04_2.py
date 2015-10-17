n=int(input('n='))
a=[]
if n>21:
    while n>1:
        i=2
        while True:
            if n%i==0:
                a.append(i)
                n//=i
                break
            else:
                i+=1
    print(a)
else:
    print('type n>21')
