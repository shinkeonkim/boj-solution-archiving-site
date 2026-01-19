import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

N, K = mii()

a = 1
b = 1

for i in range(max(K, N - K) + 1 , N + 1):
  a *= i
for j in range(1, min(K, N - K) + 1):
  b *= j

s = str(a // b)
print(s.count("0"))