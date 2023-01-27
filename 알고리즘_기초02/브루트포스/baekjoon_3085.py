#NO.3085 사탕 게임
import sys 
input = sys.stdin.readline

def check(arr):
    n = len(arr)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in  range(1,n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else: cnt = 1
            
            if cnt > ans:
                ans = cnt
        cnt = 1
        for j in  range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else: cnt = 1
            
            if cnt > ans:
                ans = cnt

    return ans


n = int(input())
arr = []
ans = 1
for _ in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            t = check(arr)
            if t > ans:
                ans = t
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            t = check(arr)
            if t > ans:
                ans = t
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(ans)