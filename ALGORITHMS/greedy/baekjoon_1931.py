#NO.1931 회의실 배정
import sys 
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int,input().split())))
meeting = sorted(meeting, key=lambda a: a[0])
meeting = sorted(meeting, key=lambda a: a[1])

last = 0
cnt = 0
for i, j in meeting:
    if i >= last:
        cnt += 1
        last = j
print(cnt)