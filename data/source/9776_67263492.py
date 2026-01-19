PI = 3.14159
ans = 0

for i in range(int(input())):
    category, *l = input().split()

    if category == "C":
        r, h = float(l[0]), float(l[1])
        ans = max(ans, 1/ 3 * PI * r * r * h)
    elif category == "L":
        r, h = float(l[0]), float(l[1])
        ans = max(ans, PI * r * r * h)
    else:
        r = float(l[0])
        ans = max(ans, 4 / 3 * PI * r**3)

print("%.3f" % ans)