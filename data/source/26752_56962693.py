h, m, s = map(int, input().split())

d = (h * 3600 + m * 60 + s + 1) % 86400

h = d // 3600
m = (d % 3600) // 60
s = d % 60

print(f"{h:02d}:{m:02d}:{s:02d}")