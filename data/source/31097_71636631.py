import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  y, m, d = mii("-")
  
  arr = [
    [3, 21, 19, "Aries"],
    [4, 20, 20, "Taurus"],
    [5, 21, 20, "Gemini"],
    [6, 21, 22, "Cancer"],
    [7, 23, 22, "Leo"],
    [8, 23, 22, "Virgo"],
    [9, 23, 22, "Libra"],
    [10, 23, 22, "Scorpio"],
    [11, 23, 21, "Sagittarius"],
    [1, 20, 18, "Aquarius"],
    [2, 19, 20, "Pisces"]
  ]
  
  for i, j, k, ret in arr:
    if (m == i and d >= j) or (m == i + 1 and d <= k):
      return ret
  
  return "Capricorn"

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    ret = solve()
    p(ret)