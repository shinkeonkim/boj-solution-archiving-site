import sys
l = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

s = 0
for i in range(int(input())):
	k = int(input())
	s += k
	l[k] -= 1

a = b = 0
#if s >= 21:
#	print("DOSTA")
#	sys.exit()


for i in range(2, 12):
	if s + i <= 21:
		a += l[i]
	else:
		b += l[i]

print("VUCI" if a > b else "DOSTA")