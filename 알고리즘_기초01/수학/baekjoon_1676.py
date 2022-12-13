#NO. 1676 팩토리얼 0의 개수
import sys
input = sys.stdin.readline

def fact(a):
    if a <= 1:
        return 1
    return a * fact(a-1)

n = str(fact(int(input())))
cnt = 0
for i in n[::-1]:
    if i != '0': break
    cnt += 1
print(cnt)

# 5로 나누어 떨어지는 수가 몇개인지 구하는 방법 <<효율적>>
# n = int(input())
# def five_count(n):
#     cnt = 0
#     while n != 0:
#         n //= 5
#         cnt += n
#     return cnt

# print(five_count(n))