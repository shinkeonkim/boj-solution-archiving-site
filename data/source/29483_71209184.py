d = {"H": 1, "C": 12, "N": 14, "O": 16}

s = input()
ans=0
i = 0
while i < len(s):
	k = d[s[i]]
	if i + 1 < len(s) and s[i + 1] not in "HCNO":
		k *= int(s[i+1])
		i+=1
	i+=1
	ans+=k
print(ans)