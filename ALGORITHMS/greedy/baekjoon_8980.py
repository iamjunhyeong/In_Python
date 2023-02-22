#NO.8980 택배 (15점)
import sys 
input = sys.stdin.readline

n, maxi = map(int,input().split())
m = int(input())
boxs = [list(map(int,input().split())) for _ in range(m)]
boxs.sort()

stack = []
capa = 0
cnt = 0
for i in range(n):
    #박스 하차
    e = 0
    while stack:
        if e >= len(stack):
            break
        if stack[e][1] == (i+1):
            cnt += stack[e][2]
            capa -= stack[e][2]
            stack.pop(e)
        else:
            e += 1
    #박스 상차
    for s in range(m):
        if boxs[s][0] > (i+1):
            break
        if boxs[s][0] == (i+1) and capa < maxi:
            a = capa + boxs[s][2]
            if a >= maxi:
                boxs[s][2] -= (a - maxi)
            capa += boxs[s][2]
            stack.append(list(boxs[s]))
print(cnt)