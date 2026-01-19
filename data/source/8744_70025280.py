n = int(input())
l = [*map(int, input().split())]

flag = [0, 0, 0, 0, 0]

d = [
  [0, 1, 2],
  [0, 1],
  [1, 2],
  [0, 2],
  [2],
]

for i in l:
  for j in range(5):
    if flag[j] >= len(d[j]):
      continue
    if i == d[j][flag[j]]:
      flag[j] += 1

print(max(flag))