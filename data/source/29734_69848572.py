N, M = map(int, input().split())
T, S = map(int, input().split())

c1 = N // 8 - (0 if N % 8 else 1)
c2 = M // 8 - (0 if M % 8 else 1)

a = N + c1 * S
b = M + c2 * S + (2 * c2 + 1) * T

if a < b:
  print("Zip")
  print(a)
else:
  print("Dok")
  print(b)