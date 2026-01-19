n, m = map(int, input().split())

crt = [*map(int, input().split())]
past = [*map(int, input().split())]

ans = max(past[i] - crt[i] for i in range(min(n, m)))
ans = max(ans, max(past[n:] + [0]))

print(ans)
