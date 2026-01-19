import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  c, b, n, r = mii()
  if b == 0:
    input()
    chk_list = []
  else:
    chk_list = mii()
  l = [mii() for _ in range(n)]
  
  ans = 0
  
  for company, money in l:
    if company in chk_list:
      ans += int(money * r / 100)
  
  return ans
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
    
    print(f"Data Set {t}:")
    print(d)
    print()
