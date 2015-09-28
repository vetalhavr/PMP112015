n=int(abs(input("n=")))
print n
s=0
while n>0:
  s=s+n%10
  n=n/10
print "suma:"
print s
