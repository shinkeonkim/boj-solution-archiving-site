a, b, c = map(int, input().split())

if a == c:
    print(f"{a}{b}{c}")
elif b == c:
    print(f"{a}{b}{b}{a}")
else:
    print(f"{a}{b}{c}{b}{a}")
