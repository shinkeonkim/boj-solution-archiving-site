L = []
n=int(input())
for i in range(n):
    K = list(map(int,input().split()))
    L.append(K)
L.sort(key = lambda t : t[0])
D = [1]*n
for i in range(n):
    for j in range(i+1,n):
        if L[i][1] <L[j][1] and D[j] < D[i]+1:
            D[j]=D[i]+1
print(n-max(D))