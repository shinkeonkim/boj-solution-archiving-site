n = int(input())
m = int(input())

l = list(map(int, input().split()))
d = {}

for i in l:
  d[i] = 1

ans = 0

for i in l:
  if m - i == i:
    continue

  if d.get(m - i, 0) == 0:
    continue

  ans += 1

print(ans // 2)
