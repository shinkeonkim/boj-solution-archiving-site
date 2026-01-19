import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

l = [mii() for i in range(4)]
s = set()

for i in range(4):
  s.add(sum(l[i][:]))
  s.add(sum(l[:][i]))

print("magic" if len(s) == 1 else "not magic")