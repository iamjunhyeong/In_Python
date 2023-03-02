#NO.16956 늑대와 양
# 울타리 최소갯수를 세는 문제가 아니므로 울타리를 무한대로한다
r, c = map(int,input().split())
graph = [list(input()) for _ in range(r)]

#늑대 옆에 양이 있을경우
sign = False
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0<=nx<r and 0<=ny<c and graph[nx][ny] == 'S':
                    sign = True
                    break
        elif graph[i][j] == 'S':
            continue
        elif graph[i][j] == '.':
            graph[i][j] = 'D'
if sign == True:
    print(0)
else:
    print(1)
    for i in graph:
        print(''.join(i))