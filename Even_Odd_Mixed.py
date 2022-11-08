n=int(input())
even=0
odd=0
r=0
while n>0:
    r=n%10
    if r%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
if even>0 and odd<=0:
    print("Even")
elif even<=0 and odd>0:
    print("Odd")
elif even>0 and odd>0:
    print("Mixed")