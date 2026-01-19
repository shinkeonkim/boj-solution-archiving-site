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
    s = input()
    
    if s == "0":
      break
    
    crt = 2
    ans = 0
    for i in s[::-1]:
      ans += int(i) * (crt - 1)
      crt *= 2
    print(ans)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
