#NO.16194 카드구매하기2
import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int,input().split()))
d = [0 for _ in range(n+1)]

for i in range(1,n+1):
    d[i] = cards[i]
    for k in range(1,i+1):
        t = d[k] + cards[i-k]
        if t < d[i]:
            d[i] = t

print(d[n])