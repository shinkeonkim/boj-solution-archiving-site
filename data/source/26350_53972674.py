for i in range(int(input())):
    n, *l = map(int, input().split())
    
    l.sort()
    
    chk = True
    
    for j in range(0, n - 1):
        if l[j + 1] < 2* l[j]:
            chk = False
            break
    
    print("Denominations:", *l)
    if chk:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
