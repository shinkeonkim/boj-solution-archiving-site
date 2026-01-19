for _ in range(int(input())):
  n = int(input())
  l = [[*map(int, input().split())] for i in range(n)]
  
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  flag = False
  
  for i in range(n):
    for j in range(n):
      if l[i][j] == 0:
        flag = True
        break
      
      for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
          continue
        
        if l[i][j] == l[ny][nx]:
          flag = True
          break
    
    
    if flag:
      break

  print("YES" if flag else "NO")