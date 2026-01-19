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

def solve():
  while 1:
    s = input()
    if s == '#':
      break
    s = s.split()[1]
    
    chk = []
    ans = []
    
    for i in range(1, len(s)):
      if s[i] == s[i - 1] and s[i] not in chk:
        chk.append(s[i])
    
    chk.sort()
    for i in chk:
      ans.append(f"{i} {i} glued")
    if len(ans) > 0:
      p(*ans, sep=" and ")
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   