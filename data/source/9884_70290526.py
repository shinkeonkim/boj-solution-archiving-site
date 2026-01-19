def f(a, b):
    return f(b, a % b) if b else a

a, b = map(int, input().split())
print(f(a,b))