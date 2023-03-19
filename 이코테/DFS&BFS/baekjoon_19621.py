#NO.19621 회의실 배정2
#참고 : https://jinho-study.tistory.com/926
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
graph.sort()
res = []
#마지막 시작 시간
last_start = max([s for s, e, c in graph])

def dfs(i,cnt):
    cnt += graph[i][2]
    if graph[i][1] > last_start:
        res.append(cnt)
    for j in range(i+1,n):
        # 이전 끝나는 시간이 다음시작시간보다 많으면
        if graph[i][1] > graph[j][0]:
            continue
        dfs(j,cnt)
        
for i in range(n):
    dfs(i,0)
print(max(res))