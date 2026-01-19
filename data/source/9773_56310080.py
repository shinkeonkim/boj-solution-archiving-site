for i in range(int(input())):
  s = input()
  a = sum([*map(int, list(s))])
  b = int(s[-3:]) * 10
  
  id = a + b
  
  if id < 1000:
    id += 1000
  
  id %= 10000
  
  print(f"{id:04d}")
