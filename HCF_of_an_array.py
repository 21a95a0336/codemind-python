import math
def gcd(n,m):
    h=max(n,m)
    s=min(n,m)
    for i in range(h,-1,-1):
        if h%i==0 and s%i==0:
            return i
n=int(input())
l=[int(i)for i in input().split()]
hcf = 0
for i in l:
    hcf=gcd(hcf,i)
print(hcf)