#NO.2133 타일 채우기
n = int(input())
dp = [0] * 31
dp[2] = 3
for i in range(4,31,2):
    dp[i] += 3*dp[i-2]
    for j in range(4, i, 2):
        dp[i] += 2*dp[i-j]
    dp[i] += 2
print(dp[n])


# n=2 : 3
# n=4 : 11
# n=6 : 41
# n=8 : 153