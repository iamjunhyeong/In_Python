#NO.1463 1로 만들기 (오답)
import sys 
input = sys.stdin.readline

X = int(input())
cnt = 0

while X != 1:
    if X%3 == 0:
        X //= 3
        cnt += 1
    elif (X-1)%3 == 0:
        X -= 1
        cnt += 1
    elif X%2 == 0:
        X //= 2
        cnt += 1
    else:
        X -= 1
        cnt += 1

print(cnt)