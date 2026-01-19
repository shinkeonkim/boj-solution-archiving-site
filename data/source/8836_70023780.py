for i in range(int(input())):
  n, k = map(int, input().split())
  
  if n <= k:
    print(k - n)
    continue
  
  n -= k
  if n % (k - 1) == 0:
    print(0)
  else:
    print(k - (n % (k - 1)) - 1)