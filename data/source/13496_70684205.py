import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


for tc in range(ii()):
  n, speed, d = mii()
  
  l = [mii() for _ in range(n)]
  
  ans = 0
  
  for dis, val in l:
    left_day = dis // speed + int(dis % speed > 0)
    
    if left_day <= d:
      ans += val
  
  print(f"Data Set {tc+1}:")
  print(ans)
  print()
    