import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


# g: 그룹의 수
# p: 그룹당 사람 수
# t: 얼마나 많은 그룹이 개별로 테스트되어야 하는지
g, p, t = mii()

a = g * p
b = g + t * p

print(1 if a < b else (2 if a > b else 0))