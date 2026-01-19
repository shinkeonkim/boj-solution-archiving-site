a, b = map(int, input().split())
k, x = map(int, input().split())
l = k - x
r = k + x

if r < a or b < l:
  print("IMPOSSIBLE")
else:
  print(min(b, r) - max(a, l) + 1)