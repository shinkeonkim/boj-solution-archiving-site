def f(s):
  c = s[:-1].count('1')
  
  if c % 2 == int(s[-1]):
    return True
  
  return False


for i in range(int(input())):
  s = input()
  ans = 0
  
  for j in range(0, len(s), 8):
    ret = f(s[j:j+8])
  
    if not ret:
      ans += 1
  print(ans)
  