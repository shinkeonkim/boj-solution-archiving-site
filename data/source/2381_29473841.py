import sys
Z = []
L = [list(map(int,input().split())) for i in range(int(input()))]
if len(L) == 1:
    print(0)
    sys.exit()

L.sort(key = lambda t: t[0])
Z.extend([L[0],L[1], L[-1],L[-2]])
L.sort(key = lambda t: -t[0])
Z.extend([L[0],L[1], L[-1],L[-2]])
L.sort(key = lambda t: t[1])
Z.extend([L[0],L[1], L[-1],L[-2]])
L.sort(key = lambda t: -t[1])
Z.extend([L[0],L[1], L[-1],L[-2]])
L.sort(key = lambda t: t[0]+t[1])
Z.extend([L[0],L[1], L[-1],L[-2]])
L.sort(key = lambda t: t[0]-t[1])
Z.extend([L[0],L[1], L[-1],L[-2]])

ans = 0
for i in range(len(Z)):
    for j in range(i+1, len(Z)):
        a = Z[i]
        b = Z[j]
        ans = max(ans, abs(a[0]-b[0])+abs(a[1]-b[1]))
print(ans)
