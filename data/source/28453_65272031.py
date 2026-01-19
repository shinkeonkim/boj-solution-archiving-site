def f(n):
	if n == 300:
		return 1
	if n >= 275:
		return 2
	if n >= 250:
		return 3
	return 4

n = int(input())
print(*[f(i) for i in [*map(int,input().split())]])