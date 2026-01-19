import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())

tc = 1
while 1:
  n = ii()
  
  if n < 0:
    break
  
  l = [mii() for _ in range(n)]
  inp()
  
  m_x = sum([i[0] * i[2] for i in l])
  m_y = sum([i[1] * i[2] for i in l])
  m_sum = sum([i[2] for i in l])
  

  print(f"Case {tc}: {m_x / m_sum:.2f} {m_y / m_sum:.2f}")

  
  tc += 1