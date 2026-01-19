import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


for i in range(100, 1000):
  for j in range(i + 1, 1000):
    if (i % 10) != (j // 100):
      continue
    if i * (j % 100) == (i // 10) * j:
      print(f"{i} / {j} = {i // 10} / {j % 100}")
