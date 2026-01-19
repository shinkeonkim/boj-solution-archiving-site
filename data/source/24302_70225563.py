import sys

input = sys.stdin.readline

def f(x):
  x = x // 1000 * 1000

  if x <= 5000:
    return 400
  if x <= 10000:
    return 700
  if x <= 20000:
    return 1200
  if x <= 30000:
    return 1700
  return 57 * (x // 1000)

def g(x):
  x = x // 1000 * 1000
  k = x // 1000
  if x <= 2000:
    return 90 + 90 * k
  if x <= 5000:
    return 100 + 85 * k
  if x <= 20000:
    return 125 + 80 * k
  if x <= 40000:
    return 325 + 70 * k
  return 925 + 55 * k

a, b = map(float, input().split())

print("{:.2f}".format((min(f(a), g(a)) + min(f(b), g(b)))/100))