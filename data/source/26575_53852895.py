def init(s):
    if s[0] == ".":
        s = "0" + s
    return float(s)

for _ in range(int(input())):
    d, f, p = map(init, input().split())
    
    ans = d * f * p
    
    print(f"${ans:.2f}")
    