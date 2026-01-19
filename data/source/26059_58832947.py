n, x = input().split()
a, b = map(int, x.split(","))

mx = [-1, -1]
ans = "-1"

for i in range(int(n)):
    s, x = input().split()
    
    c, d = map(int, x.split(","))
    
    if a >= c and b >= d:
        if mx[0] * 100 + mx[1] < c * 100 +d:
            mx = [c, d]
            ans = s

print(ans)
