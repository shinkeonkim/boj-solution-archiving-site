INF = 10000000000000
def f(i):
    return -1 if i == INF else i

n = int(input())
l = sorted([*map(int, input().split())])

a, b = [INF] * 2

for i in range(1, n):
    diff = l[i] - l[i - 1]
    
    if diff % 2 == 0:
        a = min(a, diff)
    else:
        b = min(b, diff)

for i in range(2, n):
    diff = l[i] - l[i - 2]
    
    if diff % 2 == 0:
        a = min(a, diff)
    else:
        b = min(b, diff)
print(f(a), f(b))