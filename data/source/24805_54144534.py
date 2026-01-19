a, b, h = map(int, input().split())
cnt = 0

while h > 0:
  cnt += 1
  h -= a
  
  if h <= 0:
    break

  h += b

print(cnt)
