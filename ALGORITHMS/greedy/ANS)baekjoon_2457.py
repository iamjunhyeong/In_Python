#NO.2457 공주님의 정원
import sys 
input = sys.stdin.readline

n = int(input())
date = []
for _ in range(n):
    m1,d1,m2,d2 = map(int, input().split())
    s = m1*100 + d1
    e = m2*100 + d2
    date.append([s,e])
date.sort()
cnt = 0
end = 0
target = 301

res = n
while date:
    if target >= 1201 or target < date[0][0]:
        break

    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]

            date.remove(date[0])
        else:
            break

    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
