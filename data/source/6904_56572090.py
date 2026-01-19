while 1:
  n = int(input())
  
  if n == 0:
    break
    
  t = 1
  
  mn = 9876543210
  ans = (0, 0)  
  
  while t * t <= n:
    if n % t > 0:
      t += 1
      continue
      
    l = 2 * t + n // t * 2
    
    if l < mn:
      mn = l
      ans = (t, n // t)

    t += 1

  print(f"Minimum perimeter is {mn} with dimensions {ans[0]} x {ans[1]}")
