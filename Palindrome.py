n=int(input())
temp=n
sum=0
r=0
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if sum==n:
    print("True")
else:
    print("False")