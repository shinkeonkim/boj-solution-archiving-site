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
  s = input().split()
  
  ans = 0
  for i in range(len(s)):
    crt = s[i]
    
    if s[i] == "u" or s[i] == "ur":
      ans += 1
    
    if s[i] == "of" and i > 0:
      if s[i - 1] in ["should", "would"]:
        ans += 1
    
    ans += int("lol" in crt)
  
  p(ans * 10)

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
        
