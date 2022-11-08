def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=1
            return False
    if count==0:
        return True
a=int(input())
t=0
for i in range(1,a):
    if prime(i):
        for j in range(1,a):
            if prime(j):
                if i*j==a:
                    t=1
                    print(i,end=" ")
                    print(j,end=" ")
                    break
        if t==1:
            break
if t==0:
    print("-1")