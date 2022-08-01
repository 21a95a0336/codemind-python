x=int(input())
s=0
p=1
c=0
while x>0:
    r=x%10
    r1=r*r
    s+=r1
    x=x//10
    if s>4 and x==0:
        x=s
        s=0
print(s==1)
        
    