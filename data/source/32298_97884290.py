n, m = map(int, input().split())
print(*[i for i in range(m * 2, m * 2 + n * m, m)])