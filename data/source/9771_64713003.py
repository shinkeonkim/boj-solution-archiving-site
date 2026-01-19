o = input()

ans = 0
while(1):
    try:
        s = input()
    except:
        break
    ans += s.count(o)
print(ans)
