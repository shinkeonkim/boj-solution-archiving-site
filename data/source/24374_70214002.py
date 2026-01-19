def f(num, k):
  ret = 0
  for i in num:
    ret *= k
    a = 0
    
    if '0' <= i <= '9':
      a = int(i)
    else:
      a = 10 + ord(i) - 65
    
    if a >= k:
      return -1
    
    ret += a
  return ret


x, c = input().split("=")
a,b = x.split("+")

for i in range(2, 37):
  if f(a, i) + f(b, i) == f(c, i):
    print(i)
    break