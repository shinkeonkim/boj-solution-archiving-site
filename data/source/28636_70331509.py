import sys

input = sys.stdin.readline

ans = 0
for i in range(int(input())):
  h, m = map(int, input().split(":"))
  ans += h * 60 + m
d = (ans // 3600)
h = (ans % 3600) // 60
m = ans % 60
print("{:02d}:{:02d}:{:02d}".format(d, h, m))