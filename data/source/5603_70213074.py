def f(a):
  crt = a[0]
  cnt = 1
  
  ret = ""

  for i in range(1, len(a)):
    if a[i] == crt:
      cnt += 1
    else:
      ret += str(cnt)+str(crt)
      cnt = 1
      crt = a[i]
  ret += str(cnt)+str(crt)
  
  return ret

n = int(input())
s = input()

for _ in range(n):
  s = f(s)
  
print(s)