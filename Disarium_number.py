n=a = int(input())

k = str(n)
su = 0
su1=0
m = len(k)


while n>0:
    r = n%10
    su = r**m
    su1 = su1+su
    n = n//10
    m = m-1
if su1==a:
    print('True')
else:
    print('False')

    

        