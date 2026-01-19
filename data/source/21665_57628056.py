n,m=map(int,input().split())

l = [input() for i in range(n)]
input()
l2 = [input() for i in range(n)]

ans=0
for i in range(n):
    for j in range(m):
        if l[i][j] == l2[i][j]:
            ans += 1
print(ans)
    