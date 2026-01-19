n = int(input())

t1 = n // 100 * 100 + 99
t2 = (n // 100 - 1) * 100 + 99

print(t1 if t2 < 0 or abs(t1 - n) <= abs(t2 - n) else t2)
