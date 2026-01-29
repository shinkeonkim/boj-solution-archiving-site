"""
[30320: Better Chance](https://www.acmicpc.net/problem/30320)

Tier: Silver 5
Category: math, arithmetic
"""

from math import floor

def round_up_half(n): return floor(n + 0.5)

def f(k):
  return round_up_half(float(k) * 100)


def solve():
  r_t, r_j, s_t, s_j = input().split()
  r_t = int(r_t)
  r_j = int(r_j)
  
  s_t = f(s_t)
  s_j = f(s_j)
    
  if (r_t - 1) * s_j == (r_j - 1) * s_t:
    print("SAME")
  elif (r_t - 1) * s_j < (r_j - 1) * s_t:
    print("TAOYUAN")
  else:
    print("JAKARTA")

solve()
