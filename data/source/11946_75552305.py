import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
	n, m, q = mii()

	ac = {}
	time = {} # 키: (팀, 문제)
	total_time = {}
	wa = {} # 키: (팀, 문제)

	submissions = [input().split() for _ in range(q)]

	for t, team, problem, result in submissions:
		t = int(t)
		team = int(team)
		problem = int(problem)
	
		if time.get((team, problem), -1) >= 0:
			continue

		if result == "AC":
			penalty = wa.get((team, problem), 0)

			time[(team, problem)] = t + 20 * penalty
			total_time[team] = total_time.get(team, 0) + time[(team, problem)]
			ac[team] = ac.get(team, 0) + 1
		else:
			wa[(team, problem)] = wa.get((team, problem), 0) + 1
	
	ret = [[_+1, 0, 0] for _ in range(n)] # 팀번호, 문제 수, 총 시간

	for k, v in ac.items():
		ret[k - 1][1] = v
	
	for k, v in total_time.items():
		ret[k - 1][2] = v

	ret.sort(key = lambda t : (-t[1], t[2], t[0]))

	for i in ret:
		p(*i)


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()