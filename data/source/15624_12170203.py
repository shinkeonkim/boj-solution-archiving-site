n=input()
n=int(n)

b=[0,1]
for i in range(2,n+1):
    b.append((b[i-1]+b[i-2])%1000000007)
print(b[n]%1000000007)