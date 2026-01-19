l = []
ans = 0

while 1:
    s = input()
    
    if s == '#':
        break
    
    
    if s == '0':
        ans = 0
        for k in l:
            z = k.split()
            mile = int(z[-2])
            class_code = z[-1]
            
            if class_code == 'F':
                ans += mile * 2
            elif class_code == 'B':
                ans += mile + (mile + 1) // 2
            elif 1 <= mile <= 500:
                ans += 500
            else:
                ans += mile
        print(ans)
                        
        l = []
        continue

    l.append(s)
    
    