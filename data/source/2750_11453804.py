a=input()
a=int(a)
b=[]

for i in range(0,a):
    c=input()
    c=int(c)
    b.append(c)
    
b.sort()

for i in b:
    print(i,end="\n")