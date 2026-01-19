n = int(input())
l = [*map(int, input().split())]
d = sorted([[i, l[i], 0] for i in range(n)], key = lambda t : t[1])

crt = 1
d[0][2] = 1

for i in range(1, n):
  if d[i][1] == d[i-1][1]:
    d[i][2] = crt
  else:
    d[i][2] = crt = i + 1

ans = [0] * n

for i in range(n):
  ans[d[i][0]] = d[i][2]

for rank in ans:
  print(rank)
