l=[*map(int,input().split())]
t=sum(l)//3
ans = 0

if l[0] > t:
  d = l[0] - t
  l[1] += d
  ans += d

if l[2] > t:
  d = l[2] - t
  l[1] += d
  ans += d

ans += l[1] - t

print(ans)
