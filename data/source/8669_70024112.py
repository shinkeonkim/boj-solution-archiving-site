import sys
n = int(sys.stdin.readline())
l = [[*map(int, sys.stdin.readline().split())] for i in range(n)]

mx = {}
cnt = {}

for c, info in l:
  _mx = mx.get(info, -1)
  
  if _mx < c:
    mx[info] = c
    cnt[info] = 1
  elif _mx == c:
    cnt[info] = cnt.get(info, 0) + 1

print(len(cnt))
# print(sum(cnt.values()))