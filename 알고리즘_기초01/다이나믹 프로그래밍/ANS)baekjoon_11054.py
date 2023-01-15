#NO.11054 가장 긴 바이토닉 부분 수열
x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] -1

print(max(result))

## 오답
# n = int(input())
# arr = list(map(int,input().split()))
# dp = [1] * n

# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[j]+1,dp[i])

# k = dp.index(max(dp))
# for i in range(k,n):
#     for j in range(i):
#         if arr[i] < arr[j]:
#             dp[i] = max(dp[j]+1,dp[i])

# print(max(dp))