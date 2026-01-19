mn = 2 * 10 ** 9
mx = 0
sm = 0

for i in range(int(input())):
  a, b = map(int, input().split())
  mn = min(a / b, mn)
  mx = max(a / b, mx)
  sm += a / b

print(mn, mx, sm)
