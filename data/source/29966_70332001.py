import sys

input = sys.stdin.readline

n = int(input())
a = ""
b = ""
l = sorted(list(input()), reverse=True)

for i in range(n):
  if i % 2 == 0:
    a += l[i]
  else:
    b += l[i]

print(int(a[::-1]) + int(b[::-1]))