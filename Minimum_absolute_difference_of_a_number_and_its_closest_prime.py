def prime(x):
    s=0
    for i in range(1,x+1):
        if (x%i==0):
            s+=1
    if s==2:
        return True
    else:
        return False
def b(x):
    while prime(x)!=True:
        x=x-1
    return x
def a(x):
    while prime(x)!=True:
        x=x+1
    return x
x=int(input())
p=b(x)
q=a(x)
n=abs(x-p)
m=abs(x-q)
print(min(n,m))
    