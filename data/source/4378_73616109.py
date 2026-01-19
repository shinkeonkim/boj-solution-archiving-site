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
  l = [
    "`1234567890-=",
    "QWERTYUIOP[]\\",
    "ASDFGHJKL;'",
    "ZZXCVBNM,./"
  ]
  
  while 1:
    try:
      s = input()
    except:
      break
    for i in s:
      for j in l:
        if i in j:
          p(end=j[j.index(i) - 1])
          break

      else:
        p(end=i)
    p()  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

