n, m = map(int, input().split())
s = 0
for i in range(n):
    if "+" in input():
        s += 1
print(s)