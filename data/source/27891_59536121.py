# s = input()

# s = s.replace(" ", "")
# s = s.replace(".", "")
# s = s.lower()[:10]

# print(s)

d = [
    ["northlondo", "NLCS"],
    ["branksomeh", "BHA"],
    ["koreainter", "KIS"],
    ["stjohnsbur", "SJA"]
]

s = input()

for a, ans in d:
    d = [*set([abs(ord(s[i]) - ord(a[i])) for i in range(len(s))])]
    
    if len(d) == 1 or (len(d) == 2 and d[0] + d[1] == 26):
        print(ans)
        break
