import sys

input = sys.stdin.readline

h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))
d = h2 * 60 + m2 + 1440 - (h1 * 60 + m1)
print("{:02d}:{:02d}".format(d//60, d%60))