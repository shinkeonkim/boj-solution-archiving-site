a, b = map(float, input().split())
C = 299792458

b *= -1

print((a - b) / (1 - (a * b) / (C * C)))
