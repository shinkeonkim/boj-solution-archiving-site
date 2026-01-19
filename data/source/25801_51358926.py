s = input()

d = {}
for i in s:
    try:
        d[i] += 1
    except:
        d[i] = 1

a = 0
b = 0

for cnt in d.values():
    if cnt % 2:
        b += 1
    else:
        a += 1

if a == 0:
    print(1)
elif b == 0:
    print(0)
else:
    print("0/1")