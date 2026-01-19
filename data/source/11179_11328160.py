a=input()
a=str(bin(int(a)))
b=list(a)
b=b[2 : ]
b.reverse()

c=""
for i in b:
    c=c+i

A=int(c,2)
print(A)