n = int(input())
l = [*map(int, input().split())]

mx = max(l)
mn = min(l)

for i in l:
  print(max(abs(mx - i), abs(mn - i)))
