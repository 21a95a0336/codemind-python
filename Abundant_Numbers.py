n=int(input())
temp=0
r=0
sum=0
t=0
temp=n
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("True")
else:
    print("False")