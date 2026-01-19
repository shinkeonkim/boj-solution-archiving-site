for i in range(int(input())):
    l = [*map(int, input().split())]
    cnt = sum(i >= 10 for i in l)
    
    print(*l)
    print(["zilch", "double", "double-double", "triple-double"][cnt])
    print()
   