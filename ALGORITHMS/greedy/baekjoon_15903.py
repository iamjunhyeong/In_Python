#NO.15903 카드 합체 놀이
from heapq import *
import sys 
input = sys.stdin.readline

n, m = map(int,input().split()) #카드 개수 , 병합횟수
qu = list(map(int,input().split()))
heapify(qu) # 힙으로 바꿔줌

for i in range(m):
    a,b = heappop(qu),heappop(qu)   #가장 작은 수 두개 반환
    heappush(qu,a+b)    # 두개 병합 후 다시 2번 푸쉬
    heappush(qu,a+b)
print(sum(qu))