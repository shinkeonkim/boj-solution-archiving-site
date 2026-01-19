k, a, b = map(int, input().split())

if a * b > 0:
  if a > 0:
    # 둘다 양수 범위
    print(b // k - a // k + (1 if a % k == 0 else 0))
  else:
    a = -a
    b = -b
    print(a // k - b // k + (1 if b % k == 0 else 0))
    # 둘다 음수 범위
elif a * b == 0:
  if a == 0:
    print(b // k + 1)
    # 양수 범위
  else:
    print((-a) // k + 1)
    # 음수 범위    
else:
  print((-a) // k + b // k + 1)
