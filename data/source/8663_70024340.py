n, m = map(int, input().split())

d = 0
cnt = 0

while m > 0 and d < n:
  d += m
  cnt += 1
  m //= 2

if d < n:
  cnt += n - d

print(cnt)