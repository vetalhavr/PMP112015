n=int(raw_input('n='))
a=float(raw_input('a='))
s=0
k=1
if n>=k:
    for k in range(1,(n+1)):
        s1=(k**2)*a**(k-1)
        s=s+s1
else:
    print "Error"
print 'result=',s

        

        
