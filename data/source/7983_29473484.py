N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
L.sort(key=lambda t : (-t[1], -t[0]))

crt = L[0][1] - L[0][0]
for d, t in L[1:]:
    if t < crt:
        crt = t
    crt -= d
print(crt)
