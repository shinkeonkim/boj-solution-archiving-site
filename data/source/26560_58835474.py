for i in range(int(input())):
    s = input()
    n = len(s) - 1
    
    while s[n] == '.' and n >= 0:
        n -= 1
    
    print(s[:n+1]+".")