import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(key, s):
  ret = 0
  for i in key:
    ret += s.count(i)
  return ret
  

def solve():
  s = input().lower()
  
  a = f(s, "kangaroo")
  b = f(s, "kiwibird")
  
  if a > b:
    p("Kangaroos")
  elif a < b:
    p("Kiwis")
  else:
    p("Feud continues")

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

