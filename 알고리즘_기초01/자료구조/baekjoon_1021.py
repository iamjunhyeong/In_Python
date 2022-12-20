#NO.1021 회전하는 큐
from collections import deque

n, k = map(int,input().split())
nums = list(map(int,input().split()))
queue = deque(list(range(1,n+1)))
res = 0

for num in nums:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        elif queue.index(num) < len(queue)-queue.index(num):
            res += queue.index(num)
            queue.rotate(-(queue.index(num)))
        else:
            res += len(queue)-queue.index(num)
            queue.rotate(len(queue)-queue.index(num))

print(res)