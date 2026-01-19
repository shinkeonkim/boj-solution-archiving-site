while 1:
  a, b = input().split()
  if a == b == '0':
    break
  s = True
  
  ans = ""
  
  for i in b:
    if i == a:
      continue
      
    if i != '0':
      s = False

    if s and i == '0':
      continue

    ans += i

  print(0 if ans == "" else ans)