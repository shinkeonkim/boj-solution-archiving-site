import sys
input = sys.stdin.readline

from math import pi, sqrt

a = float(input())

r = sqrt(a / pi)

print((2 * r + 2) ** 2)