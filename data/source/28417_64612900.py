n = int(input())

ans = 0

for i in range(n):
    l = [*map(int, input().split())]
    ans = max(ans, max(l[0:2]) + sum(sorted(l[2:])[-2:]))
print(ans)