#NO.9465 스티커
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int,input().split())))
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]
    for i in range(2,n):
        arr[0][i] += max(arr[1][i-1],arr[1][i-2])
        arr[1][i] += max(arr[0][i-1],arr[0][i-2])

    print(max(arr[0][n-1], arr[1][n-1]))
