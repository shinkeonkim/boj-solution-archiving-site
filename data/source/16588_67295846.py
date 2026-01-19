a = sorted(list(input()))
b = sorted(list(input()))

i = j = 0

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        i += 1

if j == len(b):
    print("YES")
else:
    print("NO")