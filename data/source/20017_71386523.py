n, m, a = map(int, input().split())
l = [*map(int, input().split())]

ans = 0
for i in range(m, n * m):
	if l[i - m] * 2 < l[i]:
		ans += 1
print(a * ans)