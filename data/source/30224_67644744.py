n = input()
d = int(n) % 7 == 0
print((3 if d else 2) if "7" in n else int(d))