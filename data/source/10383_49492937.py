tc = 0
while 1:
  tc += 1

  n = int(input())
  if n == 0:
    break

  words = []

  while 1:
    words.extend(input().split())

    if len(words) == n:
      break

  words = sorted([[words[i], i] for i in range(n)], key=lambda t:t[0])

  ans = 0
  for i in range(n):
    ans += abs(words[i][1] - i)

  print(f'Site {tc}: {ans}')
