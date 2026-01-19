import sys
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
ii = lambda : int(input())

y,m,d = mii("-")
k = ii()
d = y * 360 + (m - 1) * 30 + (d - 1) + k
print("{}-{:02d}-{:02d}".format(d // 360, (d % 360) // 30 + 1, d % 30 + 1))
