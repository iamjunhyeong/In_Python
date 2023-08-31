import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

li = sorted(li)

for i in range(m):
	l, r = 0, n - 1
	flag = 0
	while l <= r:
		mid = (l + r) // 2
		if li2[i] == li[mid]:
			flag = 1
			break
		elif li2[i] > li[mid]:
			l = mid + 1
		elif li2[i] < li[mid]:
			r = mid - 1
	if flag:
		print(1)
	else:
		print(0)