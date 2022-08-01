x=int(input())
def rev(x):
    l=list(str(x))
    l=l[::-1]
    return ''.join(l)
r=int(rev(x))
i=0
c=0
while r>0:
    t=r%10
    if t==6:
        c+=1
    if c==1 and t==6:
        t=9
    i=i*10+t
    r=r//10
print(i)
        