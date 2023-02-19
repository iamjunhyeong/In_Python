#NO.2170 선긋기
import sys 
input = sys.stdin.readline

n = int(input())
li = [tuple(map(int,input().split())) for _ in range(n)]
li.sort()

# 첫번째 두점 빼기
start = li[0][0]
end = li[0][1]
cnt = end - start

for i in range(1,n):
    #이전의 끝점이 지금의 시작점보다 크다면 스킵
    if end > li[i][1]:
        continue
    #이전의 끝점과 지금의 시작점 중 더 큰점을 기준으로 길이재기
    #합계 += (지금의끝점) - (기준점)
    if end < li[i][0]:
        cnt += li[i][1] - li[i][0]
    else:
        cnt += li[i][1] - end
    end = li[i][1]
print(cnt)