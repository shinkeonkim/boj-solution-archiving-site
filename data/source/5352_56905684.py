for _ in range(int(input())):
  n, m = map(int, input().split())
  
  l = [input() for i in range(n)]
  D = [[0] * m for i in range(n)]
  ans = 0

  for i in range(n):
    for j in range(m):
      if i > 0:
        D[i][j] = max(D[i][j], D[i - 1][j])
      if j > 0:
        D[i][j] = max(D[i][j], D[i][j - 1])
        
      if l[i][j] == 'C':
        D[i][j] += 1
    ans = max(ans, max(D[i]))
  print(ans)
  