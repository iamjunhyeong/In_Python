n = list(input())
l = 'abcdefgh'

x = l.index(n[0])+1
y = int(n[1])

dx = [2, -2, 1, -1]
dy = [[1,-1],[1,-1],[2,-2],[2,-2]]

cnt = 0
for i in range(4):
    for j in range(2):
        fx = dx[i] + x
        fy = dy[i][j] + y
        if fx > 0 and fy > 0 and fx < 9 and fy < 9:
            cnt += 1

print(cnt)