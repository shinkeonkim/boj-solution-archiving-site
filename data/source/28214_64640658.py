n,k,p=map(int,input().split())
l=[*map(int,input().split())]

a=0
for i in range(n):
    s=0
    for j in range(k):
        s+=l[i*k+j]
    if p > k-s:
        a+=1
print(a)