import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []

def dfs(num):
	if len(li) == m:
		print(*li, sep=' ')
	else:
		for i in range(num, n + 1):
			li.append(i)
			dfs(i + 1)
			li.pop()

dfs(1)

# while i + m <= n + 1:
# 	j = i + 1
# 	for _ in range(m):
# 		li = []
# 		li.append(i)
# 		for k in range(m - 1):
# 			li.append(j)
# 			j += 1
# 		print(*li, sep=' ')
# 		if j > n: break
# 	i += 1