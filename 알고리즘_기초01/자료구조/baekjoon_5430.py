from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    a = input().rstrip()[1:-1].split(",")
    queue = deque(a)
    rev = 0
    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if not queue:
                print("error")
                break
            if rev % 2 == 0:
                queue.popleft()
            else:
                queue.pop()
    else:
        if rev % 2 == 0:
            print('['+','.join(queue)+']')
        else:
            queue.reverse()
            print('['+','.join(queue)+']')

