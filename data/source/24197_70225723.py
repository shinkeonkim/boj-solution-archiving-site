import sys

input = sys.stdin.readline

def f(a, b, n):
  x = abs(a - b)
  return min(x, n - x)

ans = 0
n, m = map(int, input().split())
l = [1]+[*map(int, input().split())]

for i in range(1, m+1):
  ans += f(l[i - 1], l[i], n)
print(ans)