t=int(input())
for k in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                c+=1
    if c==0:
        print("0")
    else:
        k=arr[n-1]-arr[0]
        print(k)