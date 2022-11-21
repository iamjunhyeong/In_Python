# NO.1181
import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    a = input()
    li += [a]

set_li = sorted(list(set(li)))
set_li.sort(key=len)

for i in set_li:
    print(i)