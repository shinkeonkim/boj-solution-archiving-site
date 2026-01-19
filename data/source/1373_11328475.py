a=input()
a=int(a,2)
a=oct(a)

a=list(a)
a=a[2:]

for i in a:
    print(i,end='')