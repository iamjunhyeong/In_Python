#NO.11399 ATM
n = int(input())
P = list(map(int,input().split()))

P = sorted(P)
S = 0
for i in range(n):
    S += sum(P[:(i+1)])
    
print(S)