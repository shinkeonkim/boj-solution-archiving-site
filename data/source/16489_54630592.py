from math import sqrt
def f(r, x):
  return sqrt(r * r - x * x / 4)
a, b, c = map(float, input().split())

q = a + b + c
t = q / 2

S = sqrt(t * (t - a) * (t - b) * (t - c))
r = 2 * S / q
R = a * b * c / 4 / S
d = 0 if a == b == c else sqrt(R * (R - 2 * r))
k = f(R, a) + f(R, b) + f(R, c)

print(f'{S:.11f}\n{R:.11f}\n{r:.11f}\n{d:.11f}\n{k:.11f}')
