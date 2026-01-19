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
  s = """A	.-	B	-...
C	-.-.	D	-..
E	.	F	..-.
G	--.	H	....
I	..	J	.---
K	-.-	L	.-..
M	--	N	-.
O	---	P	.--.
Q	--.-	R	.-.
S	...	T	-
U	..-	V	...-
W	.--	X	-..-
Y	-.--	Z	--..
1	.----	2	..---
3	...--	4	....-
5	.....	6	-....
7	--...	8	---..
9	----.	0	-----
,	--..--	.	.-.-.-
?	..--..	:	---...
-	-....-	@	.--.-.
  """
  
  l = s.split()
  d = {}
  
  for i in range(0, len(l), 2):
    d[l[i+1]] = l[i]
  
  n = ii()
  k = input().split()
  
  ans = ""
  for i in k:
    ans += d[i]
  p(ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
