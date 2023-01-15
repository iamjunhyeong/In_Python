#NO.11722 가장 긴 감소하는 부분 수열
n = int(input())
arr = list(map(int,input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
