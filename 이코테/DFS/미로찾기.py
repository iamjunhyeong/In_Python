n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
x = 0
y = 0
cnt = 0
while x != n-1 or y != m-1:
    if x < n and graph[x+1][y] == 1:
        x += 1
        cnt += 1
    elif y < m and graph[x][y+1] == 1:
        y += 1
        cnt += 1
cnt += 1
print(cnt)
