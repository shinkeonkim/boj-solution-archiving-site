def f(n):
  if n < 4:
    return n

  c = 1
  s = 1
  
  while s < n:
    s *= 2
    c += 1
  
  return c

print(f(int(input())))