while 1:
  a = int(input())
  
  if a == 0:
    break
    
  print("TENTE NOVAMENTE" if a % 42 else "PREMIADO")