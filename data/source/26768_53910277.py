s = input()
d = "a4e3i1o0s5"

for i in range(5):
    s = s.replace(d[2*i], d[2*i+1])

print(s)
