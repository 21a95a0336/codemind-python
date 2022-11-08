s=input()
count=0
for character in s:
    if character.isdigit():
        count=count+1

if count>0:
    print("Contains",count,"digit")
else:
    print("Doesn't contain digit")