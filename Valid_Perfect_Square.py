import math
t=int(input())
sqr=0
while t>0:
    n=int(input())
    sqr=int(math.sqrt(n))
    if sqr*sqr==n:
        print("True")
    else:
        print("False")
    t=t-1