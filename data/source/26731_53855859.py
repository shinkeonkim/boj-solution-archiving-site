a = "".join(sorted([*input()]))
i = 65
j = 0

while j < 25:
    if i != ord(a[j]):
        print(chr(i))
        break
    i += 1
    j += 1
else:
    print("Z")
