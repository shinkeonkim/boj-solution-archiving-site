for _ in range(int(input())):
    name, s, e = input().split()
    s, e = int(s), int(e)
    
    print(name[:s]+name[e:])