for i in range(int(input())):
  l = input().split()[1:]
  cnt = 0
  ans = 0
  for char in l:
    if char == 'X':
      cnt += 1
      ans = max(ans, cnt)
    else:
      cnt = 0

  print(f'The longest contiguous subsequence of X\'s is of length {ans}')
