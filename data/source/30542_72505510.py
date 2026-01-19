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
  s = input().lower()
  k = ""
  for i in s:
    if 'a' <= i <= 'z':
      k += i
  
  for i in range(len(k)):
    for j in range(2, len(k)+1):
      a = k[i:i + j]
      if len(a) < 2:
        continue
      
      if a == a[::-1]:
        p("Palindrome")
        return
  p("Anti-palindrome")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   