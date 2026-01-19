import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


def f(s):
  if len(s) <= 2:
    return False
  
  if s[:2] != "io":
    return False
  
  for i in s[2:]:
    if '0' <= i <= '9':
      continue
    return False
  
  return True
  

s = input()

print("Correct" if f(s) else "Incorrect")