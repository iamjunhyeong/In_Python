#NO.1456 거의소수
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
MAX = 10000001
li = [True] * MAX
li[0] = False
li[1] = False

#에라토스테네스의 체 사용
for i in range(2,int(MAX**0.5)+1):
    if li[i] == False: 
        continue
    for j in range(i+i,MAX,i):
        li[j] = False

cnt = 0
for i in range(2, MAX):
    if not li[i]:           # 소수가 아니라면 넘기기
        continue

    for j in range(2,int(b**0.5)+1):        # 소수의 2제곱부터 범위 내에 값 찾기
        if a <= i**j <= b:
            cnt += 1
            j += 1
        if i**j>b: break
print(cnt)