#NO.1026 보물
import sys 
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

bb = sorted(b)
aa = sorted(a, reverse=True)

S = 0
for i in range(n):
    S += aa[i] * bb[i]
print(S)