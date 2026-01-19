n, x = map(int, input().split())
l = [*map(int, input().split())]

ans = 9999999999999999999
for i in range(1, n):
    ans = min(ans, (l[i-1]+l[i])*x)
print(ans)