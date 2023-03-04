#NO.1325 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    cnt = 1
    visited = [0] * (n+1)
    qu = deque()
    qu.append(s)
    visited[s] = 1
    while qu:
        a = qu.popleft()
        for i in computer[a]:
            if visited[i]:
                continue
            qu.append(i) 
            visited[i] = 1
            cnt += 1
    return cnt

n, m = map(int,input().split())
computer = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    # a가 b를 신뢰한다 == b를 해킹하면 a도 해킹가능하다.
    computer[b].append(a)

maxx = 0
ind = []
for i in range(1,n+1):
    cnt = bfs(i)
    #최대값 몇인지 구하기
    if maxx < cnt and cnt > 0:
        maxx = cnt
    # 일단 모두 저장
    ind.append([i,cnt])

#모두 저장한거에서 최대값과 같으면 출력
for i, cnt in ind:
    if cnt == maxx:
        print(i, end=' ')
