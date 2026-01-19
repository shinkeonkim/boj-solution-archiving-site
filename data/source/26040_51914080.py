s = input()
l = input().split(' ')
ans = ""

for i in s:
	ans += i.lower() if i in l else i

print(ans)
