cnt = 0

for i in range(int(input())):
  s = input().lower()

  if 'pink' in s or 'rose' in s:
    cnt += 1

print(cnt if cnt > 0 else 'I must watch Star Wars with my daughter')
