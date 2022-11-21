# NO.18870
import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li_set = sorted(list(set(li)))
dic = {}
for i in range(len(li_set)):
    dic[li_set[i]] = i

for i in li:
    print(dic[i], end=' ')