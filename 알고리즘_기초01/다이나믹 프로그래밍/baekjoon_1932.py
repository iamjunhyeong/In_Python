#NO.1932 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
dp = [0]
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1,n+1):
    dp.append(list([0]*i))
dp[1] = arr[1]
for i in range(2,n+1):
    for j in range(i):
        if j == 0:
            dp[i][0] = dp[i-1][0] + arr[i][0]
        elif j == i-1:
            dp[i][j] = dp[i-1][j-1] +arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + arr[i][j]
print(max(dp[n]))