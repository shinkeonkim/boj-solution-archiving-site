n = int(input())
l = [int(input()) for i in range(n)]

s = sum(l)

for i in l:
    if 2 * i == s:
        print(i)
        break
else:
    print("BAD")