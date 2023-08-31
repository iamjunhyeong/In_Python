import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(0 for _ in range(n))

t = 0
d = k - 1
res = []
while True:
	if li[d] == 0:
		li[d] = 1
		res.append(d + 1)
		t += 1
	if t == n:
		break
	j = 0
	while j != k:
		d = (d + 1) % n
		if li[d] == 0:
			j += 1
print("<" + ", ".join(map(str, res)) + ">")

