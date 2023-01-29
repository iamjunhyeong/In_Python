#NO.4948 베르트랑 공준
import math

def checkValue(n):
    if n == 1:
        return True
    else:
        for comp in range(2, int(math.sqrt(number))+1):
            if n % comp == 0:
                return False
    return True

value = list(range(123456*2))
prime_number = list()

for number in value:
    if checkValue(number):
        prime_number.append(number)

while True:
    insertN = int(input())
    cnt = 0

    if insertN == 0:
        break

    for valueN in prime_number:
        if insertN < valueN <= insertN*2:
            cnt += 1
    print(cnt)