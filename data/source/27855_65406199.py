a, b = map(int, input().split())
c, d = map(int, input().split())

a = 3 * a + b
c = 3 * c + d

if a > c:
    print(1, a - c)
elif a < c:
    print(2, c - a)
else:
    print("NO SCORE")
