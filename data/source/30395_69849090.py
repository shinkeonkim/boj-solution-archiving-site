n = int(input())
l = [*map(int, input().split())]

frz = True
mx = 0
crt = 0
use_time = -2

for i in range(n):
  if i == use_time + 2:
    frz = True
  
  if l[i] == 0:
    if frz:
      frz = False
      use_time = i
    else:
      crt = 0
  else:
    crt += 1
    mx = max(mx, crt)
print(mx)
