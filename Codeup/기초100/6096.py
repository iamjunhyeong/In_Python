graph = [list(map(int,input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    for j in range(19):
        if graph[a-1][j] == 0:
            graph[a-1][j] = 1
        else:
            graph[a-1][j] = 0
    for i in range(19):
        if graph[i][b-1] == 0:
            graph[i][b-1] = 1
        else:
            graph[i][b-1] = 0
        
for g in graph:
    print(*g, sep=' ')