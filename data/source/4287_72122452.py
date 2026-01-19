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
    if s == "#":
      break
    
    a, b, c = s.split()
    ans = ""
    for i in range(len(a)):
      k = ord(b[i]) - ord(a[i])
      
      d = chr(((ord(c[i]) - 97 + k + 26) % 26) + 97)
      ans += d
    p(a, b, c, ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
