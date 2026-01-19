tc = 1
while 1:
    l = [*map(int, input().split())]
    
    if l[0] == 0:
        break
    l = l[1:]
    n = len(l)
    
    if n % 2 == 0:
        d = (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        d = l[n // 2]
    
    print(f"Case {tc}: {d:.1f}")
    
    tc += 1