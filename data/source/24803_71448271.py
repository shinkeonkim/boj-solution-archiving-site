g, s, c = map(int, input().split())

d = 3 * g + 2 * s + c

l = []

if d >= 8:
	l.append("Province")
elif d >= 5:
	l.append("Duchy")
elif d >= 2:
	l.append("Estate")

if d >= 6:
	l.append("Gold")
elif d >= 3:
	l.append("Silver")
else:
	l.append("Copper")
	
print(*l, sep = " or ")