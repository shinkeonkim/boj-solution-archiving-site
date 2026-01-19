def f(s):
  return 1 if s == s[::-1] else 0

def g(s):
  ret = 0
  for i in range((len(s) + 2) // 2):
    ret += 1
    if s[i] != s[-i - 1]:
      break
  return ret

for _ in range(int(input())):
  s = input()
  
  print(f(s), g(s))
