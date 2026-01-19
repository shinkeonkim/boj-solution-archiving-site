"""
[28298: 더 흔한 타일 색칠 문제](https://www.acmicpc.net/problem/28298)

Tier: Silver 3 
Category: bruteforcing, greedy, implementation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  n, m, k = mii()

  ans = [[] for _ in range(k)]
  l = [inp() for _ in range(n)]
  
  for y in range(k):
    for x in range(k):
      d = {}
      for i in range(n // k):
        for j in range(m // k):
          char = l[y + k * i][x + k * j]
          
          d[char] = d.get(char, 0) + 1
      
      mx = 0
      crt = ""
      
      for c, cnt in d.items():
        if cnt > mx:
          mx = cnt
          crt = c
      
      ans[y].append(crt)
  
  
  cnt = 0
  
  for i in range(n):
    for j in range(m):
      cnt += (ans[i % k][j % k] != l[i][j])
  
  p(cnt)
  for i in range(n):
    for j in range(m):
      p(end=ans[i % k][j % k])
    p()

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()