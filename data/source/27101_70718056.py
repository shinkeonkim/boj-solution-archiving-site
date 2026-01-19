import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def f(n, l):
  for i in range(n):
    if l[i][i] != 0:
      return 1
  
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      if l[i][j] <= 0:
        return 2
  
  for i in range(n):
    for j in range(n):
      if l[i][j] != l[j][i]:
        return 3
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if l[i][k] + l[k][j] < l[i][j]:
          return 4
  return 0


n = ii()
l = [[*map(int, input().split())] for _ in range(n)]

print(f(n, l))