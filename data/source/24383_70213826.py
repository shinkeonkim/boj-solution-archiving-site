ans = set()
s = input()
cnt = 0

for i in s:
  if i == '0':
    cnt += 1
  else:
    if cnt != 0:
      ans.add(cnt)
      cnt = 0
if cnt > 0:
  ans.add(cnt)
print(len(ans))