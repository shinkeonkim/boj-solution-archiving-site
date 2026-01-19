import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


t1, t2 = mii() # 시작 시간
t3 = ii() # 등록시간(분)

t4, t5 = mii() # 이동 시간
br = ii() # 학생 수
t6 = ii() # 한명을 수용하는데 걸리는 시간


move = t4 * 60 + t5 + (br + 1) * t6 + t3 + 10


ref = t1 * 60 + t2

k = ref - move

print(f"{k // 60:02d} {k % 60:02d}")
