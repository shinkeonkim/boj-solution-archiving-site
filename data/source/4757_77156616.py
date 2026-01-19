import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n = ii()

  teams = [inp().split() for _ in range(n)]

  # name, 각 문제당 제출 횟수, 최종 AC 시간

  result = []

  for i in range(n):
    team = teams[i]

    name = team[0]

    ac_count = 0
    penalty_sum = 0

    for idx in range(1, 5):
      time = int(team[idx * 2])
      penalty = int(team[idx * 2 - 1])

      if time == 0:
        continue

      ac_count += 1
      penalty_sum += (penalty - 1) * 20 + time

    result.append([name, ac_count, penalty_sum])

  result.sort(key = lambda t:(-t[1], t[2]))

  p(*result[0])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()