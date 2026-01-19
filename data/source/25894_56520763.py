for tc in range(1, int(input()) + 1):
  d = {}
  
  for __ in range(int(input())):
    a, b = input().split()
    d[a] = b
  
  print(f"Test case #{tc}:")
  
  d = d.items()
  for __ in range(int(input())):
    s = s2 = input()

    for a, b in d:
      s = s.replace(a, b)
    
    if s == s[::-1]:
      print(s2, "YES")
    else:
      print(s2, "NO")
  print()