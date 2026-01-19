import sys

n = int(input())

l = [[*map(int, input().split())] for i in range(n)]

if n == 2:
  print("1 1")
  sys.exit()

ans = [0] * n

ans[0] = (l[0][1] + l[0][2] - l[1][2]) // 2

for i in range(1, n):
  ans[i] = l[0][i] - ans[0]

print(*ans)
