n,m = map(int,input().split())
ice = []

for _ in range(n):
    ice.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            res += 1

print(res)