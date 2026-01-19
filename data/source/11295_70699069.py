import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

k = 0

while 1:
  k += 1
  L = ii()
  
  if L == 0:
    break
    
  N = ii()
  l = [ii() for _ in range(N)]
  
  
  print(f"User {k}")

  for i in l:
    s = L * i
    print(f"{s // 100000}.{s%100000:05d}")