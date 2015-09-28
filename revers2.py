n=int(abs(input("n=")))
s=''
while n>0:
  s=s+str(n%10)
  n=n/10
print "revers:"
print s
