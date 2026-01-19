l = [input() for i in range(int(input()))]
s = []
for i in l:
  if len(i) == 3:
    s.append(i)
s.sort()

print(s[0])