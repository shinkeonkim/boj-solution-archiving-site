from datetime import datetime

crt = datetime(*map(int, input().split("-")))
ans = 0

for i in range(int(input())):
    d = datetime(*map(int, input().split("-")))

    if d >= crt:
        ans += 1
print(ans)