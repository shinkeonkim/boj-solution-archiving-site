def f():
  s = int(input())

  for i in range(s + 1):
    for j in range(s + 1):
      if i * i + j * j == s:
        return i, j
  
  return -1, -1

def g(a, b):
  if a == b == -1:
    print("Impossible")
    return

  print(0, 0)
  print(-a, b)
  print(b, a)
  print(b - a, a + b)


a, b = f()
g(a, b)
