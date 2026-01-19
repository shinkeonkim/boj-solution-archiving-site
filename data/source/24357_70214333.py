l = [[*map(int, input().split())] for i in range(3)]
D = [[0] * 3 for i in range(3)]
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

for i in range(3):
  for j in range(3):
    if l[i][j] == 9:
      D[i][j] = 9
      continue

    cnt = 0
    for d in range(8):
      ny = i + dy[d]
      nx = j + dx[d]
      
      if ny < 0 or nx < 0 or ny >= 3 or nx >= 3:
        continue
      if l[ny][nx] == 9:
        cnt += 1
    D[i][j] = cnt

for i in range(3):
  print(*D[i])