def f(a):
  return a if a > 0 else 0

def g(a, mi):
  if a % 2 and f(a / 2 - mi) != 0:
    return "{:.1f}".format(f(a / 2 - mi))
  else:
    return str(f(a // 2 - mi))

c, z, n = map(int, input().split())
l = [int(input()) for i in range(6)]
d = [l[3] + l[4] * 2 + l[5], l[0] * 2 + l[1] + l[5], l[1] + l[2] * 2 + l[3]]

print(g(d[0], c),end=" ")
print(g(d[1], z),end=" ")
print(g(d[2], n),end=" ")
