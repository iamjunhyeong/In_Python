# No.4948 베르트랑 공준
def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

value = list(range(2,123456*2))
prime = []

for i in value:
    if isPrime(i):
        prime.append(i)

while True:
    n = int(input())
    cnt = 0

    if n == 0:
        break

    for i in prime:
        if n < i <= n*2:
            cnt += 1
    print(cnt)        