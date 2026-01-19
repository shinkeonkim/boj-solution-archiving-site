def f():
  n = int(input())
  
  for c in range(-n, n + 1):
    if c == 0 or n % c:
      continue
    for d in range(-n, n + 1):
      if d == 0 or (n + 2) % d:
        continue
        
      a = n // c
      b = -(n + 2) // d
      
      if a*c == n and b * c + a * d == n + 1 and b * d == - (n + 2):   
        return [a, b, c, d]
  return [-1]

print(*f())
