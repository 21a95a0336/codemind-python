def cl(x):
    c=0
    b=x
    while x!=0:
        a=x%10
        c=c*10+a
        x=x//10
    return (b==c)
def b(x):
    if cl(x)==True:
        x=x-1
    while cl(x)!=True:
        x=x-1
    return x
def a(x):
    if cl(x)==True:
        x=x+1
    while cl(x)!=True:
        x=x+1
    return x
x=int(input())
#print(x)
n=b(x)
m=a(x)
if abs(x-n)<abs(x-m):
    print(n)
elif abs(x-n)>abs(x-m):
    print(m)
else:
    print(n,m,end=' ')
        