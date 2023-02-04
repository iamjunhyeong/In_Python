#NO.11047 동전0
import sys 
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
cnt = 0
for _ in range(n):
    coin.append(int(input()))
for i in range(n-1,-1,-1):
    if k == 0:
        break
    if k < coin[i]:
        continue
    cnt += k // coin[i]
    k %= coin[i]

print(cnt)