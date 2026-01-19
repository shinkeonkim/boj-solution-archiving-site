a, b, c , d = map(int, input().split())
a = a* b
b = c* d

if a > b:
    print("M")
elif a < b:
    print("P")
else:
    print("E")