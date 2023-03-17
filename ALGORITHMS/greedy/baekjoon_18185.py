#NO.18185 라면사기(small)
#참고 : https://blog.koderpark.dev/30
import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) +[0,0]
cnt = 0

# 세개 살때
def triple(i):
    global cnt
    k = min(arr[i:i+3])
    arr[i] -= k
    arr[i+1] -= k
    arr[i+2] -= k
    cnt += (k*7)

#두개 살때
def double(i):
    global cnt
    k = min(arr[i:i+2])
    arr[i] -= k
    arr[i+1] -= k
    cnt += (k*5)

#하나 살때
def one(i):
    global cnt
    k = arr[i]
    arr[i] -= k
    cnt += (k*3)

for i in range(n):
    # 세번째보다 두번째가 큰 경우 두개를 먼저 사준다.
    # 1 2 1 1 일 경우 -> 0 1 1 1 -> 0 0 0 0 
    # 12원만에 살수 있다.
    if arr[i+1] > arr[i+2]:
        k = min(arr[i],arr[i+1]-arr[i+2])
        arr[i] -= k
        arr[i+1] -=k
        cnt += (k*5)
        triple(i)
    else:
        triple(i)
        double(i)
    one(i)
print(cnt)