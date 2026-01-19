import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  d = [
    "@", "8", "(", "|)", "3", "#", "6", "[-]",
    "|", "_|", "|<", "1", "[]\\/[]", "[]\\[]",
    "0", "|D", "(,)", "|Z", "$", "']['", "|_|",
    "\\/", "\\/\\/", "}{", "`/", "2"
  ]
  
  s = input()
  ans = ""
  
  for i in s:
    if 'A' <= i <= 'Z':
      ans += d[ord(i) - 65]
    elif 'a' <= i <= 'z':
      ans += d[ord(i) - 97]
    else:
      ans += i
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
