import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

a = int(input())
b = int(input())

ans = 0
for i in range(1, a + 1):
  for j in range(1, b + 1):
    if i + j == 10:
      ans += 1

print(f"There {'is' if ans == 1 else 'are'} {ans} way{'' if ans == 1 else 's'} to get the sum 10.")