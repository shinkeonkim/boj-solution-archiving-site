A,B=map(int,input().split())
n=int(input())
L=list(map(int,input().split()))
S=0
k=[]
for i in range(n):
    S+=L[i]*(A**(n-i-1))

while(S>0):
    k.append(S%B)
    S//=B

for i in range(len(k)-1,-1,-1):
    print(k[i],end=" ")