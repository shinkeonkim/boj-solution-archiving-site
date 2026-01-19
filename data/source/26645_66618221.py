def f(n, s, e, k):
  i = n
  j = 0
  while s <= i <= e and j < k:
    i += 1
    j += 1
  
  return i


n = int(input())

ans = 4
mx = n + 1

crt = f(n, 200, 229, 2)
if crt > mx:
  mx = crt
  ans = 3

crt = f(n, 200, 219, 4)
if crt > mx:
  mx = crt
  ans = 2

  
crt = f(n, 200, 209, 8)
if crt > mx:
  mx = crt
  ans = 1
print(ans)
