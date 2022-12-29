#NO.11052 카드구매하기
import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int,input().split()))
d = [0 for _ in range(n+1)]

for i in range(1,n+1):
    for k in range(1,i+1):
        d[i] = max(d[i], d[i-k] + cards[k])

print(d[n])