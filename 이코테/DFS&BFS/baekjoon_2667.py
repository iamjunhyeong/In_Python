#NO.2667 단지번호붙이기
n = int(input())
graph = []
num = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

cnt = 0
res = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(cnt)
            res += 1
            cnt = 0

num.sort()
print(res)
for i in num:
    print(i)

