a, b = map(int, input().split())

ans = 0

while a != b:
  ans += 1
  a, b = max(a, b) - min(a, b), min(a, b)

print(ans)