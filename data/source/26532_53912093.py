a, b = map(int, input().split())

s = a * b

print(s // 24200 + (1 if s % 24200 else 0))