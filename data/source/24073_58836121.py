n = input()
s = "IOI"
s2 = input()

idx = 0
for i in s2:
    if s[idx] == i:
        idx += 1
    
    if idx == 3:
        print("Yes")
        break
else:
    print("No")