for i in range(int(input())):
    s = input()
    
    print(end=s[0])
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        print(end=s[i])
    
    print()