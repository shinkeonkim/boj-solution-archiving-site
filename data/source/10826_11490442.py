a=input()
a=int(a)

ar=[0,1,1,2]

for i in range(4,a+1):
    ar.append(ar[i-1]+ar[i-2])

print(ar[a])
