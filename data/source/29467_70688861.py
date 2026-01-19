import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

s = input()
d = []

for i in range(len(s)):
  for j in range(i + 1, len(s)+1):
    d.append(s[i:j])

d.sort()

print(d[-1])