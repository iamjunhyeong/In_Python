#NO.1747 소수&팰린드롬
MAX = 1000001
n = int(input())

prime = [1] * MAX
prime[0] = 0
prime[1] = 0
#에라토스테네스의 체
for i in range(2,int(MAX**0.5)+1):
    if not prime[i]:
        continue
    for j in range(i+i,MAX,i):
        prime[j] = 0

res = 0
for i in range(n,MAX):
    if not prime[i]:
        continue
    if str(i) == str(i)[::-1]:  # 팰린드롬 확인 
        res = i
        break

if res == 0:
    res = 1003001       
    # N의 범위만 한정되어있을뿐, 출력값에 범위가 정해져있는 것이 아니므로 
    # N이 범위를 벗어나도 최솟값이 없을땐 범위 이상의 최솟값이 1003001를 출력
print(res) 

