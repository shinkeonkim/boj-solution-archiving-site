n = int(input())
l = [*map(int, input().split())]

crt = 1
ans = 0
for i in l:
  if i == crt:
    crt += 1
  else:
    ans += 1
print(ans)
