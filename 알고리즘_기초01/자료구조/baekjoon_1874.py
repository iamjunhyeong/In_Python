# NO.1874 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
li1 = []
li2 = []
num = 1
flag = 1

for i in range(N):
    n = int(input())
    while num <= n:
        li1.append(num)
        li2.append('+')
        num += 1
    if li1[-1] == n:
        li1.pop()
        li2.append('-')
    else:
        flag = 0
if flag == 0:
    print("NO")
else:
    for i in li2:
        print(i)
