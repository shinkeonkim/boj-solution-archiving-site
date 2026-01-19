ans = 0
for i in range(2023, int(input()) + 1):
  k = str(i)
  d = "2023"
  a = b = 0
  
  while a < len(k) and b < 4:
    if k[a] == d[b]:
      b += 1
    a += 1
      
  
  if b == 4:
    ans += 1
print(ans)
