n, w = map(int, input().split())
l = [*map(int, input().split())]

ans = 0
crt = 0

for i in l:
  if i + crt >= w:
    ans += 1
    crt = 0
  else:
    crt += i
print(ans)