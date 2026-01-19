a = input()
b = input()

i = j = 0
s = ""

while i < len(a) and j < len(b):
  if a[i] < b[j]:
    s += a[i]
    i += 1
  else:
    s += b[j]
    j += 1

s += a[i:]
s += b[j:]

print(s)