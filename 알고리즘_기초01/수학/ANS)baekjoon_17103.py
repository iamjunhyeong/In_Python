#NO.17103 골드바흐 파티션
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
m = max(nums)
L= [False, False] + [True] * (m-1)
j = 2

for i in range(2,int(m**0.5)+1):
    if L[i]:
        for j in range(i*i,m+1,i):
            if L[j]:
                L[j] = False

for num in nums:
    cnt = 0
    for i in range(2, (num//2)+1):
        if L[i] and L[num-i]:
            cnt += 1
    print(cnt)
