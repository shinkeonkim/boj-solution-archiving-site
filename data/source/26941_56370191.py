n = int(input())
s = 0
crt = 1

while s + (2 * crt - 1) ** 2 <= n:
  s += (2 * crt - 1) ** 2
  crt += 1

print(crt - 1)
