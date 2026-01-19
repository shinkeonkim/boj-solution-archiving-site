import sys
input = sys.stdin.readline

n = int(input())
tm = 0

for _ in range(n):
  h, m = map(int, input().split())
  tm += h * 60 + m

mn = 10000000000000000

for i in range(20):
  for j in range(20):
    if i * 240 + j * 180 >= tm:
      mn = min(mn, i * 1090 + j * 915)
print("{:.2f}".format(mn / 100))