def gcdd(x,y):
    i=1
    gcd=0
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gcd=i
        i+=1
    return gcd
n=int(input())
arr=list(map(int,input().split()))
lcm=arr[0]
gcd=arr[0]
for i in range(1,len(arr)):
    gcd=gcdd(lcm,arr[i])
    lcm=(lcm*arr[i])//gcd
print(lcm)