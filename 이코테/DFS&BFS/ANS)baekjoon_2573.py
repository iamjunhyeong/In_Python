from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visit_tmp = [i[:] for i in visit]
    tmp = pos.pop(); pos.add(tmp)
    q = deque([tmp])
    a,b = tmp
    visit_tmp[a][b] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for a,b in move:
            dx=x+a; dy=y+b
            if visit_tmp[dx][dy] or not board[dx][dy]:
                continue
            visit_tmp[dx][dy] = True
            cnt+=1
            q.append((dx,dy))
    
    # 빙산 분리, 종료
    if cnt != len(pos):
        print(t)
        sys.exit()

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
pos = set()
for i in range(1,n):
    for j in range(1,m):
        if board[i][j] > 0:
            pos.add((i,j))

move = [(0,1),(1,0),(0,-1),(-1,0)]
t = 0
melt = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]

# 이미 처음부터 분리돼있을 가능성.
# 하지만 첫 bfs를 빼도 AC를 받는 것 보니, 무조건 합쳐진 상태로 입력이 주어지나 보다.
bfs()

# 해빙 시작
while pos:
    t+=1
    rmpos = []
    # 녹을 수치
    for x, y in pos:
        for a,b in move:
            dx=x+a; dy=y+b
            if not board[dx][dy]:
                melt[x][y] += 1
    
    # 실제 해빙
    for x, y in pos:
        board[x][y] = max(0,board[x][y]-melt[x][y])
        melt[x][y] = 0
        if board[x][y] <= 0:
            rmpos.append((x,y))
            
    for i in rmpos:
        pos.remove(i)
        
    # 영역의 수
    if not pos:
        print(0)
        break
    
    bfs()
else:
    print(0)