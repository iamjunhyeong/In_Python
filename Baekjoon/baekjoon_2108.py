# No.2108
import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
cnt_li = Counter(li).most_common()
print(round(sum(li)/n))
print(li[n//2])
if len(cnt_li) > 1:                     #li가 한개 이상일 경우
    if cnt_li[0][1] == cnt_li[1][1]:    #최빈값이 여러개일 경우
        print(cnt_li[1][0])
    else:
        print(cnt_li[0][0])
else:
    print(cnt_li[0][0])
print(max(li)-min(li))


