ans = 0
l = []
mx = 0

while 1:
  try:
    s = input()
  except:
    break
  l.append(len(s))
  mx = max(mx, len(s))
  
for i in l[:-1]:
  ans += (mx - i) ** 2

print(ans)