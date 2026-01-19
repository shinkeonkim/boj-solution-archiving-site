tc = 1

while 1:
  s = [*map(int, list(input()))]
  
  if s == [0]:
    break
  
  prev = []
  crt = s
  
  while prev != crt and len(crt) % 2 == 0:
    prev = crt[::]
    crt = []
    
    for i in range(0, len(prev), 2):
      crt.extend([prev[i + 1]] * prev[i])
    
  print(f"Test {tc}: ", end="")
  print(*crt, sep="")
  tc += 1