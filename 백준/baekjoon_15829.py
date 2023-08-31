import sys
input = sys.stdin.readline

n = int(input())
li = list(input().rstrip())
asc = []
res = 0

for i in li:
    asc.append(ord(i) - 96)
for i in range(n):
	res += asc[i] * (31**i)
print(res % 1234567891)
