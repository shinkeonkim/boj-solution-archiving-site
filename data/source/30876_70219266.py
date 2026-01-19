import sys
input = sys.stdin.readline

ans = (1001, 1001)

for _ in range(int(input())):
  x, y = map(int, input().split())
  
  if y < ans[1]:
    ans = (x, y)
print(*ans)