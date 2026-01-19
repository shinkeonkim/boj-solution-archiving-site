import sys
from math import sqrt, pi, sin, factorial
from decimal import *

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def is_upper(s):
  return 'A' <= s <= 'Z'

def is_both_upper(s):
  return is_upper(s[0]) and is_upper(s[1])


def f(A, B, s):
  n = len(s)
  
  for i in range(n):
    mom = A[2*i:2*i+2]
    dad = B[2*i:2*i+2]
    
    if is_both_upper(mom) or is_both_upper(dad):
      z = A[2 * i].upper()
    else:
      z = mom+dad
    
    if s[i] in z:
      continue
    return False
  return True


def solve():
  A = input()
  B = input()
  
  n = ii()
  
  for _ in range(n):
    baby = input()
    
    if f(A, B, baby):
      p("Possible baby.")
    else:
      p("Not their baby!")
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    d = solve()
