n, m = map(int, input().split())
crt = 0
t = 0
ans = [0] * n
l = [*map(int, input().split())]

for i in range(n):
  if crt + l[i] > m:
    crt = 0
    t += 1
  crt += l[i]
  ans[i] = t

print(*ans, sep="\n")