import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  L, H = mii()
  ans = 0

  for i in range(L, H + 1):
    k = str(i)
    
    if len(k) != len(set(k)):
      continue
    
    for j in k:
      if int(j) == 0:
        break
      if i % int(j):
        break
    else:
      ans += 1
  print(ans)  
  
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
