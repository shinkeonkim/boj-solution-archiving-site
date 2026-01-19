n = int(input())
ans = 0
crt = int(input())

for i in range(n):
  a = int(input())
  d = abs(crt - a)
  ans += min(d, 360 - d)
  crt = a

print(ans)
