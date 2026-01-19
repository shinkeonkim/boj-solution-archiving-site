import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = mii()

idx = []
a_idx = []
b_idx = []

for i in range(n):
  if i % 2 == l[i] % 2:
    idx.append(i + 1)
    if i % 2:
      a_idx.append(i + 1)
    else:
      b_idx.append(i + 1)


if len(idx) == 2:
  if len(a_idx) == len(b_idx):
    print(*idx)
  else:
    print(-1, -1)
elif len(idx) > 2 or len(idx) == 1:
  print(-1, -1)
elif len(idx) == 0:
  if n > 2:
    print(1, 3)
  else:
    print(-1, -1)
  