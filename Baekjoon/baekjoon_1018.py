# No. 1018 체스판 바꾸기
def find(a,n,m):
    for i in range(n-7):
        for j in range(m-7):
            first_B = 0
            first_W = 0
            for x in range(i,i+8):
                for y in range(j,j+8):
                    if (x + y) % 2 == 0:
                        if board[x][y] != 'W':
                            first_W = first_W+1
                        if board[x][y] != 'B':
                            first_B = first_B + 1
                    else:
                        if board[x][y] != 'B':
                            first_W = first_W+1
                        if board[x][y] != 'W':
                            first_B = first_B + 1
            re.append(first_W)
            re.append(first_B)
                
n, m = map(int,input().split())
board = []
for _ in range(n):
    s = input()
    board += [s]
re = []
find(board,n,m)
print(min(re))