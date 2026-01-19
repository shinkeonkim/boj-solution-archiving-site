for i in range(int(input())):
  a, b = input().split()
  
  n = len(a)
  
  d = 0
  for j in range(n):
    d += ord(a[j]) - ord(b[j])
  
  if d > 0:
    print(f"Swapping letters to make {a} look like {b} earned {d} coins.")
  elif d < 0:
    print(f"Swapping letters to make {a} look like {b} cost {abs(d)} coins.")
  else:
    print(f"Swapping letters to make {a} look like {b} was FREE.")