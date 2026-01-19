n = int(input())
l = [*map(int, input().split())]
s = sum(l)
ans = 0

for i in l:
  if i == 0:
    ans += s
  else:
    s -= 1
print(ans)