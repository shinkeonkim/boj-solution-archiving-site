import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  t, team = s.split()
  m, s, ss = map(int, t.split(":"))
  tm = ss + s * 1000 + m * 60000
  return (tm, team)

def solve():
  while 1:
    try:
      n = ii()
      l = mii()
    except:
      break
    if n == 1:
        print(1)
        continue
    diff = l[-1] - l[-2]
    idx = n - 2

    while idx > -1:
      if l[idx + 1] - l[idx] == diff:
        idx -= 1
      else:
        break
    print(idx + 2)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()