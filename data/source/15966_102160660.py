"""
[15966: 군계일학](https://www.acmicpc.net/problem/15966)

Tier: Silver 1
Category: dp
"""


import sys

inp = lambda : sys.stdin.readline().rstrip()
mii = lambda : [*map(int,inp().split())]

MX = 1000001

def solve():
  inp()
  l = mii()
  
  dp = [0] * MX

  for i in l:
    dp[i] = dp[i - 1] + 1
  
  return max(dp)


if __name__ == "__main__":
  print(solve())
