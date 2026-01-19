a, b, c = map(int, input().split())

ans = 0
c = str(c)
for i in range(a, b + 1):
  ans += str(i).count(c)

print(ans)
