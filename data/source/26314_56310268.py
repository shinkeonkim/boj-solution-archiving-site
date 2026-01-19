for i in range(int(input())):
  s = input()
  c = sum([s.count(i) for i in "aeiou"])
  print(s)
  print(1 if c * 2 > len(s) else 0)
    