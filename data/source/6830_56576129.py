ans = ""
mn =  201
while 1:
  try:
    s, t = input().split()
  except:
    break
  t = int(t)
  
  if mn > t:
    mn = t
    ans = s
print(ans)