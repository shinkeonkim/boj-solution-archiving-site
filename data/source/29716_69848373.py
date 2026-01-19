def f(s):
  ret = 0
  for i in s:
    if i == " ":
      ret += 1
    elif 'A' <= i <= 'Z':
      ret += 4
    else:
      ret += 2
  return ret

cnt = 0
J, N = map(int, input().split())

for i in range(N):
  a = f(input())
  if a <= J:
    cnt += 1

print(cnt)
