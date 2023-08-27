#NO.1003 피보나치 함수
# hint: https://itstory1592.tistory.com/34

import sys 
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

for i in range(3, 40 + 1):
	zero.append(zero[i - 1] + zero [i - 2])
	one.append(one[i - 1] + one[i - 2])

for i in range(int(input())):
	n = int(input())
	print(zero[n], one[n])