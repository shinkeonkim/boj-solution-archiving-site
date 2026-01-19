def f(a):
    a *= 2
    return a // 10 + a % 10

s = [*map(int, list(input()))]

print("DA" if sum([s[i] if i % 2 else f(s[i]) for i in range(16)]) % 10 == 0 else "NE")