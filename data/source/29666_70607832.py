import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())


d = [
  (1,2,3),
  (4,5,6),
  (7,8,9),
  (1,4,7),
  (2,5,8),
  (0,5,8),
  (3,6,9),
]

t = input().replace(" ", "")
z = tuple(sorted([*map(int, list(t))]))

print("Unlocked" if z in d else "Locked")