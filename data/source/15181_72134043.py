import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(a, b):
  if a > b and a - b in [2, 4, 6]:
    return True
  if a < b and a + 7 - b in [2, 4, 6]:
    return True
  return False

def solve():
  while 1:
    s = input()
    
    if s == '#':
      break
    
    for i in range(1, len(s)):
      chk = f(ord(s[i]) - 65, ord(s[i - 1]) - 65)
      if not chk:
        p("Ouch! That hurts my ears.")
        break
    else:
      p("That music is beautiful.")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

