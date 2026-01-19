n, k = map(int, input().split())

l = []

while n > 0:
  l.append(n % k)
  n //= k

s = sum([*map(int, filter(None, "".join(map(str,l[::-1])).split('0')))])

l = []

while s > 0:
  l.append(s % k)
  s //=k

print(*l[::-1], sep="")
