import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def height(s):
  d1, d2 = map(int, s[:-1].split("'"))
  return d1 * 12 + d2


def solve():
  gen, dad, mom = input().split()
  
  dad = height(dad)
  mom = height(mom)
    
  ans = dad + mom
  
  ans += 5 if gen == "B" else -5
  
  mn = max(0, ans - 4)
  mx = ans + 4

  if ans % 2:
    mn = ans // 2 - 3
    mx = ans // 2 + 4
    
  else:
    ans //= 2
    mn = ans - 4
    mx = ans + 4
  
  return (mn // 12, mn % 12, mx // 12, mx % 12)
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    print(f"Case #{t}: {ret[0]}'{ret[1]}\" to {ret[2]}'{ret[3]}\"")
    
