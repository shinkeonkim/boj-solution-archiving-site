from math import pi

def f():
  r, a, b = map(int, input().split())  
  ans = 0
  
  i = 0
  while r > 0:
    ans += pi * r * r
    if i % 2:
      r //= b
    else:
      r *= a
    
    i += 1
  return ans

  
for tc in range(int(input())):
  t = f()
  
  print(f"Case #{tc+1}: {t}")