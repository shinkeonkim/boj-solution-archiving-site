def f(s):
    if s[0] == '.':
        s = '0' + s
    return float(s)

for _ in range(int(input())):
    ans = 0

    for i in range(int(input())):
        n, q, p = input().split()
        ans += int(q) * f(p)
    
    print(f'${ans:.2f}')