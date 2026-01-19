from math import sqrt

def dis(a, b):
  return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = int(input())
l = [[*map(int, input().split())]for i in range(n)]

d = []

for i in range(0, n):
  d.append(dis(l[i], l[(i + 1) % n]))

print(sum(d) - max(d))