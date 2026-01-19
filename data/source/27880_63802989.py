s=0
for i in range(4):
    a,b=input().split()
    if a == "Es":
        s+=int(b)*21
    else:
        s+=int(b)*17
print(s)