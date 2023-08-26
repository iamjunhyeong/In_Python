from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
	while (qu):
		x, y = qu.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if (0 <= nx < m and 0 <= ny < n):
				if (box[nx][ny] == 0):
					qu.append([nx,ny])
					box[nx][ny] = box[x][y] + 1

qu = deque()
for i in range(m):
	for j in range(n):
		if box[i][j] == 1:
			qu.append([i,j])

bfs()
res = 0
for i in box:
	for j in i:
		if j == 0:
			print(-1)
			exit(0)
	res = max(res, max(i))
print(res - 1)