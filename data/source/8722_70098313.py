import sys

def f(a, d):
  a -= 1
  return a // d + (1 if a % d else 0)

n, d = map(int, sys.stdin.readline().split())
mx = ans = 0

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  x = f(a, d) * f(b, d)
  
  if mx < x:
    mx = x
    ans = a * b
  elif mx == x and ans < a * b:
    ans = a * b
      
print(ans)