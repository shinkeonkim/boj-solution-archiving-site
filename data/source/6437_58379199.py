cnt = 1

while 1:
    a, b = map(int, input().split())
    
    if a == b == 0:
        break
    
    print(f"Hole #{cnt}")
    
    if b == 1:
        print("Hole-in-one.")
    else:
        l = [
            'Double eagle.',
            'Eagle.',
            'Birdie.',
            'Par.',
            'Bogey.',
            'Double Bogey.'
        ]
        print(l[min(b - a + 3, 5)])
    
    
    print()
    cnt += 1