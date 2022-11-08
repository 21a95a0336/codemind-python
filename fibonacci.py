n =  int(input())
a=0
b=1
c=a+b
temp=n
m = 3
print(a,b,c,end=' ')
while(m<n):
    a=b
    b=c
    c=a+b
    print(c,end=' ')
    m=m+1