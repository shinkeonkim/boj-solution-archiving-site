crt = 0
s, n, m = map(int, input().split())

for i in range(n+m):
  a = int(input())

  if a == 1:
    crt += 1
  else:
    crt -= 1

  if crt > s:
    s *= 2

print(s)