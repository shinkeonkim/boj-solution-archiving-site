for i in range(int(input())):
    input()
    n = [*map(int,list(input()))]
    
    n.sort(reverse=True)
    
    d = 0
    for i in range(len(n)-1):
        d *= 10
        d += n[i]
    print(d + n[-1])
    
    