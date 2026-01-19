import sys
input = sys.stdin.readline

ans = 0
a, b = map(int, input().split())

if a == 0 or b== 0:
  print(0)
  sys.exit()
s = 0
e = 100000000000000000

while s <= e:
  mid = (s + e) // 2
  a_t = (24 / a) * mid
  b_t = (24 / b) * mid
  
  if a_t + b_t > 24:
    e = mid - 1
  else:
    s = mid + 1
    ans = max(ans, mid)
print(ans)