import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
s = input()
l = [0] * 10

for i in s:
  if i == 'L':
    for idx in range(10):
      if l[idx] == 0:
        l[idx] = 1
        break
    
  elif i == 'R':
    for idx in range(9, -1, -1):
      if l[idx] == 0:
        l[idx] = 1
        break
  else:
    l[int(i)] = 0
print(*l, sep="")