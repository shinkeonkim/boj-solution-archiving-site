x, y = map(int, input().split(":"))


t = 3540 * x + 59 * y
a = t // 3600
b = (t % 3600) // 60
c = t % 60
print(f"{a:02d}:{b:02d}:{c:02d}")
