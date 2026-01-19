s = input()
u = 0
for i in range(len(s)):
  if s[i] == 'U':
    u = i
    break
f = 0
for i in range(len(s) - 1, -1, -1):
  if s[i] == 'F':
    f = i
    break

print("-" * u + "U" + "C" * (f - u - 1) + "F" + "-" * (len(s) - f - 1))