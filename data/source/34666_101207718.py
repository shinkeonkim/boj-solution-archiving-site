
import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache
from operator import itemgetter, attrgetter, mul, add, sub, truediv
from typing import List, Tuple, Dict, Set, Any, Union
from fractions import Fraction

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


Q = int(inp())

for i in range(Q):
    a, b, c, d = mii()
    
    if a > 2 or d < 50:
        print("NO")
        continue
    
    one_cnt = 0
    two_cnt = 0
    
    l = [b, c, d]
    
    for i in l:
        if {1: 100, 2:90}[a] > i * 3:
            one_cnt += 1
        
        if 21 >= i:
            two_cnt += 1
        
    
    if one_cnt >= 2 or two_cnt >= 1:
        print("YES")
    else:
        print("NO")
        