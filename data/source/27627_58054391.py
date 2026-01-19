s = input()
n = len(s)

for i in range(1, n):
    a = s[:i]
    b = s[i:]
    
    if a == a[::-1] and b == b[::-1]:
        print(a, b)
        break
else:
    print("NO")