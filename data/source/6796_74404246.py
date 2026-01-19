import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def get(s, a, b):
  if s == 'A':
    return a
  return b

def g(a, b):
  if a <= 0 and b < 0:
    return a // b
  if a >= 0 and b > 0:
    return a // b
  
  return -(abs(a) // abs(b))
  
def solve():
  A = B = 0
  
  while 1:
    s = input()
    
    if s == "7":
      break
    
    if s[0] == "1":
      _, x, n = s.split()
      n = int(n)
      if x == 'A':
        A = n
      else:
        B = n
    elif s[0] == "2":
      _, x = s.split()
      if x == 'A':
        p(A)
      else:
        p(B)
    elif s[0] == "3":
      _, x, y = s.split()
      _x = get(x, A, B)
      _y = get(y, A, B)
      
      if x == 'A':
        A = _x + _y
      else:
        B = _x + _y
    elif s[0] == "4":
      _, x, y = s.split()
      _x = get(x, A, B)
      _y = get(y, A, B)
      
      if x == 'A':
        A = _x * _y
      else:
        B = _x * _y
    elif s[0] == "5":
      _, x, y = s.split()
      _x = get(x, A, B)
      _y = get(y, A, B)
      
      if x == 'A':
        A = _x - _y
      else:
        B = _x - _y
    elif s[0] == "6":
      _, x, y = s.split()
      _, x, y = s.split()
      _x = get(x, A, B)
      _y = get(y, A, B)
      v = g(_x, _y)
      
      if x == 'A':
        A = v
      else:
        B = v
    
tc = 1

for t in range(1, tc+1):
  ret = solve()
  
