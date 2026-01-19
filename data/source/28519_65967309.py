a, b = map(int, input().split())

print(a + b if abs(a - b) <= 1 else min(a, b) * 2 + 1)