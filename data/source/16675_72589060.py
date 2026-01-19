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

def win(a, b):
  s = "RSPR"
  
  for i in range(3):
    if a == s[i] and b == s[i + 1]:
      return True
  return False

def f(A, B):
  cnt = 0
  
  for i in range(2):
    cnt = 0
    for j in range(2):
      if win(A[i], B[j]):
        cnt += 1
  
    if cnt == 2:
      return True
  return False


def solve():
  a, b, c, d = input().split()
  
  if f([a, b], [c, d]):
    p("MS")
  
  elif f([c, d], [a, b]):
    p("TK")
  else:
    p("?")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()