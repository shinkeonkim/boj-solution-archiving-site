#bkj 7576 - 토마토
import sys
from collections import deque

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while deq:
        x,y,date = deq.popleft()
        date += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if box[nx][ny] == -1:
                continue

            if box[nx][ny] == 0:
                deq.append((nx,ny, date))
                box[nx][ny] = 1

    return -1 if any(0 in row for row in box) else date-1



input = sys.stdin.readline

m,n = map(int,input().split())
box = [[*map(int,input().split())] for _ in range(n)]
deq = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            deq.append((i,j,0))

print(bfs())
