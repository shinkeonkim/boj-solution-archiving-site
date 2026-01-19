n = int(input())
l = [*map(int, input().split())]

m = int(input())
l2 = [*map(int, input().split())]

d = []
d2 = []


for i in l:
  t = i
  j = 2
  while j * j <= i and t > 1:
    while t % j == 0:
      t //= j
      d.append(j)
    j += 1
  if t > 1:
    d.append(t)

for i in l2:
  t = i
  j = 2
  while j * j <= i and t > 1:
    while t % j == 0:
      t //= j
      d2.append(j)
    j += 1
  if t > 1:
    d2.append(t)

d.sort()
d2.sort()

i = 0
j = 0
ans = 1
chk = False

while i < len(d) and j < len(d2):
  if d[i] == d2[j]:
    ans *= d[i]
    i += 1
    j += 1
  elif d[i] > d2[j]:
    j += 1
  else:
    i += 1
    
  if ans >= 1000000000:
    chk = True
  
  if chk:
    ans %= 1000000000

if chk:
  print(f"{ans:09d}")
else:
  print(ans)
