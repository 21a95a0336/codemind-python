x,y = map(int,input().split())
for i in range(1,x+1):
    if x%i==0:
        if y%i==0:
            m = i
print(m)