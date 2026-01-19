a="qwertasdfgzxcvb"

while 1:
	s = input()
	ans=0
	
	if s == '#':
		break
	
	k = s[0] in a
	
	for i in s[1:]:
		k2 = i in a
		
		if k != k2:
			ans +=1
		k=k2
	print(ans)