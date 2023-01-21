#NO 7569 토마토 
from collections import deque
import sys 
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[] for _ in range(h)]
queue = deque()
res = 0

# 3차원 리스트 작성
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,input().split())))
        for k in range(m):
            # 추가된 리스트의 원소 중 1이면 큐에 추가
            if graph[i][j][k] == 1:
                queue.append([i,j,k])

# 3차원 리스트 방향 설정
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while queue:
    x,y,z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            # 비교한 토마토에 기존 토마토 +1 => 하루 지나는 것 구현
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append([nx,ny,nz])

# 3차원 배열 분해
for i in graph:
    for j in i:
        for k in j:
            # 큐로 while문을 돌렸음에도 0이 있다면 토마토가 익지 못 하는 상황
            if k == 0:
                print(-1)
                exit()
        res = max(res,max(j))

# 처음부터 익은 토마토가 존재하고, 따라서 시작점이 1이기 때문에 res -1
print(res-1)

