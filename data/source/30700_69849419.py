s = input()
t = "KOREA"

idx = 0
for i in s:
  if i == t[idx % 5]:
    idx += 1
print(idx)
