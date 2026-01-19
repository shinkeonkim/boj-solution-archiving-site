a = b = 0

for i in range(int(input())):
    s = input()
    
    if s == "D":
        a += 1
    else:
        b += 1
    
    if abs(a-b) >= 2:
        break
print(f"{a}:{b}")
    
    