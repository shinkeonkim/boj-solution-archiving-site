import sys

T = int(sys.stdin.readline())

while(T):
  n = int(sys.stdin.readline())
  cnt = 0
  for i in range(2, n + 1):
    tmp = n

    while tmp % i == 0:
      tmp //= i
      cnt += 1

  print(cnt)

  T -= 1
