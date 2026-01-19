s = input()
z = s.count('0')
o = s.count('1')
n = len(s)


chk = [True] * n

cnt = 0
for i in range(0, n):
    if cnt == o // 2:
        break
    if s[i] == '1':
        chk[i] = False
        cnt += 1

cnt = 0
for i in range(n - 1, -1, -1):
    if cnt == z // 2:
        break
    if s[i] == '0':
        chk[i] = False
        cnt += 1

for i in range(n):
    if chk[i]:
        print(end=s[i])