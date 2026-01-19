N, M = map(int, input().split())
ans = 0
for i in range(N):
  l = [*map(int, input().split())]
  
  if 0 in l:
    continue
  ans += 1

print(ans)