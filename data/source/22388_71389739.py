while 1:
	k = input()
	
	if k == "#":
		break
	
	s, y, m, d = k.split()
	y, m, d = map(int, [y,m,d])
	s = "HEISEI"
	
	if y > 31 or (y == 31 and m > 4):
		s = "?"
		y -= 30
	
	print(s, y, m, d)