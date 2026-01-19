import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = 20
  l = mii()
  
  for _ in range(20):
  #while 1:
    k = set(l[1:])
    
    if len(k.difference({0, 1})) == 0:
      break
    
    # l2 = l[0:1] + [0] * 19
    
    for i in range(19, 0, -1):
      if l[i] < 2:
        continue
      
      l[i - 1] += l[i] // 2

      if l[i] % 2:
        l[i] = 1
      else:
        l[i] = 0
  
  return l
    
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    ret = solve()
    print(*ret)    