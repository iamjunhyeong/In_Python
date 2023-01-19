from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int,input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y)) 

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif miro[nx][ny] == 0:
                continue
            elif miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))
    return miro[n-1][m-1]

print(bfs(0,0))