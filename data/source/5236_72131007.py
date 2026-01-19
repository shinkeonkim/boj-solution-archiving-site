import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = inp()  
  
  ans = s[-1]
  
  for i in range(len(s) - 2, -1, -1):
    if s[i] > ans[-1]:
      ans += s[i]
    else:
      break
  print(f"The longest decreasing suffix of {s} is {ans[::-1]}")
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
