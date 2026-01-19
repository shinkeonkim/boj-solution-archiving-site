L=[999999999]*1100000
N=int(input())
d=[1,2,5,7]
L[0]=0
for i in range(0,N+1):
    for j in d:
        if i+j<=N and L[i+j] > L[i]+1:
            L[i+j]=L[i]+1
print(L[N])
