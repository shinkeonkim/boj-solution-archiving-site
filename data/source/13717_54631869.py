sm = 0
mx = 0
ans = ""

for i in range(int(input())):
  s = input()
  k, m = map(int, input().split())
  
  t = 0
  while m >= k:
    t += 1
    m -= k
    m += 2
  sm += t

  if t > mx:
    mx = t
    ans = s

print(sm)
print(ans)