def f(a, b):
  return (a - b) ** 2

def g(a, b):
  return sum([f(a[i], b[i]) for i in range(len(a))])

def h(a, b):
  return g(a[:4], b[:4]) * g(a[4:6], b[4:6]) * g(a[6:], b[6:])

p = [*map(int, list(input()))]

n = int(input())

l = sorted([[*map(int, list(input()))] for i in range(n)], reverse = True)

mx = h(p, l[0])
ans = 0


for i in range(1, n):
  t = h(p, l[i])
  if mx <= t:
    mx = t
    ans = i

print(*l[ans], sep="")