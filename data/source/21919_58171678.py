d = [True] * 1000001

d[0] = d[1] = False

for i in range(2, 1000001):
    if d[i]:
        for j in range(i * i, 1000001, i):
            d[j] = False

n = int(input())
l = set([*map(int, input().split())])

ret = 1
for i in l:
    if d[i]:
        ret *= i

print(-1 if ret == 1 else ret)