import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = mii()
mn = 1111111111111111111111111111111111111111111111111

for i in range(min(l), max(l) + 1):
  p_sum = m_sum = 0

  for j in l:
    if i > j:
      p_sum += (i - j)
    elif j > i:
      m_sum += (j - i)
    
  ans = min(m_sum, p_sum)
  ans += m_sum + p_sum - 2 * ans
  mn = min(mn, ans)
print(mn)