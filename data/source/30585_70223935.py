n, m = map(int, input().split())
l = [sum([*map(int, list(input()))]) for i in range(n)]
s = sum(l)
print(min(s, n * m - s))