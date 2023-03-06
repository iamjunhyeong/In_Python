#NO.4963  섬의 개수
from collections import deque
import sys
input = sys.stdin.readline

# 해당 위치에서 양옆위아래뿐만 아니라 
# 위대각선 아래대각선까지 모두 구함
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

def bfs(i,j):
    qu = deque()
    qu.append((i,j))
    graph[i][j] = 0
    
    while qu:
        x, y = qu.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    qu.append((nx,ny))
            
while True:
    w, h = map(int,input().split())
    if w == h == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
        
    