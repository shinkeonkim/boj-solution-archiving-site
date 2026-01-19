t = int(input())

for _ in range(t):
  n = int(input())
  crt = 0
  ans = 0
  for i in range(n):
    k = int(input())
    crt += k
    if k == -1 and crt <= 0:
      ans += abs(crt)
      crt = 0
  if crt > 0:
    ans += crt
  print(ans)
  