def f(n):
  while n > 0:
    if n % 10 == 0:
      return False
    n //= 10
  return True

for _ in range(int(input())):
  n = int(input())
  
  while 1:
    n += 1
    
    if f(n):
      print(n)
      break
  