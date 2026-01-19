d = {}
for i in range(int(input())):
	a = input()
	try:
		d[a] += 1
	except:
		d[a] = 1

print(max(d.values()))
