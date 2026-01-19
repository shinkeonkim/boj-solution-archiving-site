import sys

def solve():
  n = int(input())
  l = sorted([int(sys.stdin.readline()) for i in range(n)])

  if n == 0:
    return 0
    return

  d = int(n * 3 / 20 + 0.5)
  return int(sum(l[d:n-d]) / (n - 2 * d) + 0.5)


print(solve())
