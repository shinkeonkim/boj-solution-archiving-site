n, m = map(int, input().split())
d = {}
st = set()

for i in range(n):
    s = input()
    
    if len(s) < m:
        continue
    
    st.add(s)
    
    try:
        d[s] += 1
    except:
        d[s] = 1

l = list(st)

l.sort(key=lambda t: (-d[t], -len(t), t))

print(*l, sep="\n")