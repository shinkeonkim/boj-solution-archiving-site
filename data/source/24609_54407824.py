mn = 987654321000
crt = 0
for i in range(int(input())):
  crt += int(input())
  mn = min(mn, crt)

print(-mn if mn < 0 else 0)
