import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    a = inp()
    
    if a == "0":
      break
    
    b = inp()
    
    ans = ""
    
    for i in range(len(b)):
      y = ord(b[i]) - 64
      x = ord(a[i % len(a)]) - 64
      
      ans += chr((x + y + 25) % 26 + 65)
    p(ans)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
