import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  price_a, cap_a, price_b, cap_b, total = mii()
  
  ans = (0, 0, 10000000000000000)
  for cnt_a in range(0, total // cap_a + 2):
    total_b = max((total - cap_a * cnt_a), 0)
    cnt_b = total_b // cap_b + int(total_b % cap_b > 0)
    
    price = price_a * cnt_a + price_b * cnt_b

    if price < ans[2]:
      ans = (cnt_a, cnt_b, price)
  p(*ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
