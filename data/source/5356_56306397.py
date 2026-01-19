for _ in range(int(input())):
  a, b = input().split()
  a = int(a)
  
  for i in range(1, a + 1):
    print(b*i)
    b = chr((ord(b) - 65 + 1) % 26 + 65)

  print()