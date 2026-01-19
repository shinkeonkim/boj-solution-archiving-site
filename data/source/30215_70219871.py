import sys
input = sys.stdin.readline

O, A, K = map(int, input().split())

chk = False

for i in range(1, 200):
  for j in range(1, 200):
    if O == A * i + K * j:
      print(1)
      chk = True
      break
  if chk:
    break
else:
  print(0)