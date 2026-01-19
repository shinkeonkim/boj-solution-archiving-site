import sys

input = sys.stdin.readline

l = [*map(int, input().split())]
a = [*map(int, input().split())]
cnt = {}

for i in a:
  cnt[i] = cnt.get(i, 0) + 1

ans = []

for i in range(3):
  l2 = []
  
  for i in range(0, len(l), 2):
    l2.append(l[i] if cnt.get(l[i], 0) >cnt.get(l[i + 1], 0) else l[i + 1])
    
    cnt[l2[-1]] = cnt.get(l2[-1], 0) - 1
  ans.append(l2)
  l = l2
  
for i in ans[::-1]:
  print(*i)
