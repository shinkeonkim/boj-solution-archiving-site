l=sorted([int(input()) for i in range(5)])

for i in range(1,4,2):
    if l[i] != l[i-1]:
        print(l[i-1])
        break
else:
    print(l[4])

