def miro(x,y):
    if graph[x][y] == 2:
        graph[x][y] = 9
        return

    graph[x][y] = 9
    if graph[x][y+1] != 1:
        miro(x,y+1)
    elif graph[x+1][y] != 1:
        miro(x+1,y)
    else:
        return

graph = [list(map(int,input().split())) for _ in range(10)]
miro(1,1)
for g in graph:
    print(*g, sep=' ')
