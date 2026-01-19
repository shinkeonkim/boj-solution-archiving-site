for i in range(int(input())):
    a,b = map(int,input().split())
    s = 0
    while a > 0:
        if a % 2 == 1:
            s+=1
        a//=2
    if b == s % 2:
        print("Valid")
    else:
        print("Corrupt")
