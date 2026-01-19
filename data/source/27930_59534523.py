a = "KOREA"
b = "YONSEI"

x, y = 0, 0
s = input()

for i in s:
    if i == a[x]:
        x += 1
    
    if i == b[y]:
        y += 1
        
    if x == len(a):
        print(a)
        break
    if y == len(b):
        print(b)
        break