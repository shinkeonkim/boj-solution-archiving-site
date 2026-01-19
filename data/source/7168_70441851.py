import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n, m = mii()

l = [input() for _ in range(n)]

for i in range(n):
  k = 0
  ans = []
  for val in l[i]:
    if val == '#':
      k += 1
    elif k > 0:
      ans.append(k)
      k = 0
  if k > 0:
    ans.append(k)
  if len(ans) == 0:
    ans.append(0)
  print(*ans)

for i in range(m):
  k = 0
  ans = []
  for j in range(n):
    val = l[j][i] 
    if val == '#':
      k += 1
    elif k > 0:
      ans.append(k)
      k = 0
  if k > 0:
    ans.append(k)
  if len(ans) == 0:
    ans.append(0)
  print(*ans)