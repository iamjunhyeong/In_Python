h, w = map(int,input().split())
graph = [[0]*w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int,input().split())
    x -= 1
    y -= 1
    for i in range(l):
        if d == 0:
            graph[x][y+i] = 1
        else:
            graph[x+i][y] = 1

for g in graph:
    print(*g,sep=' ')