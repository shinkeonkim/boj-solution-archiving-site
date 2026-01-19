d = 0

for i in range(10):
    d = (d + int(input())) % 4

print("NESW"[d])
