n, a, b = map(int, input().split())
s = set([*map(int, input().split())] + [*map(int, input().split())])

d = set([*range(1, n + 1)])
ans = list(d - s)
print(len(ans))
print(*ans)