s=input()
v=0
c=0
w=0
d=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v+=1
    elif i>='0' and i<='9':
        d+=1
    elif i==" ":
        w+=1
    else:
        c+=1
print('Vowels: {}'.format(v))
print('Consonants: {}'.format(c))
print('Digits: {}'.format(d))
print('White spaces: {}'.format(w))