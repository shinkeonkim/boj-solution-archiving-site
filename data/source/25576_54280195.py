import sys

n, m = map(int, sys.stdin.readline().split())
l = [*map(int, sys.stdin.readline().split())]

k = [[*map(int, sys.stdin.readline().split())] for i in range(n - 1)]

cnt = sum([int(sum(abs(k[i][j] - l[j]) for j in range(m)) > 2000) for i in range(n - 1)])

print("YES" if cnt * 2 >= (n - 1) else "NO")
