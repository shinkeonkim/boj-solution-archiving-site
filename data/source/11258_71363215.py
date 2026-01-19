l = [input().split() for _ in range(6)]

while 1:
	n = input()
	
	if n == "-1":
		break
	
	ans = 0
	
	if n == l[0][0]:
		ans += int(l[0][1])
	
	for i in range(1,3):
		if n[:3] == l[i][0]:
			ans += int(l[i][1])
	
	for i in range(3,5):
		if n[3:] == l[i][0]:
			ans += int(l[i][1])
	
	if n[4:] == l[5][0]:
		ans += int(l[5][1])
	print(ans)