import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

def f(lv, s):
  if s == "miss":
    return 0
  if s == "bad":
    return 200 * lv
  if s == "cool":
    return 400 * lv
  if s == "great":
    return 600 * lv
  return 1000 * lv

lv, s = input().split()
lv = int(lv)
print(f(lv, s))
