def f(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(3)])

l = [[*map(int, input().split())] for i in range(16)]

while 1:
    try:
        d = [*map(int, input().split())]
    except:
        break
    
    ans = []
    mn = 1111111111111111
    for i in range(16):
        v = f(d, l[i])
        if mn > v:
            mn = v
            ans = l[i]

    print(f"{d[0]:>3} {d[1]:>3} {d[2]:>3} maps to {ans[0]:>3} {ans[1]:>3} {ans[2]:>3}")
        
        
    