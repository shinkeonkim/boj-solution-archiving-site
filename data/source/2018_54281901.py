n = int(input())

ans = 1

for i in range(1, n):
  t = (2 * i - 1) ** 2 + 8 * n
  
  t_s = int(t ** (1 / 2))
  
  if t_s * t_s == t:
    d = (1 - 2 * i + t_s)
    if d > 0 and d % 2 == 0:
      ans += 1
print(ans)
