for i in range(int(input())):
  s = input()
  n = len(s)
  
  print(s)
  for i in range(1, n-1):
    print(s[i] + " " * (n - 2) + s[n - i - 1])
  if n > 1:
    print(s[::-1])
