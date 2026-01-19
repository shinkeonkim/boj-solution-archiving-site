n, m = map(int, input().split())
a, b = map(int, input().split())
c, d = map(int, input().split())


if n == 1 or m == 1:
    if a == c and b == d:
        print("YES")
    else:
        print("NO")
else:
    print("YES" if (a + b) % 2 == (c + d) % 2 else "NO")