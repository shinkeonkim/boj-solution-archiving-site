n = int(input())
s = ""

for i in range(1, n+1):
    if str(i) in s:
        continue
    s += str(i)
print(s)