n, x = map(int, input().split())
t = [*map(int, input().split())]

idx = 0

while 1:
  if t[idx] < x:
    break
  
  x += 1
  
  idx = (idx + 1) % n

print(idx + 1)
