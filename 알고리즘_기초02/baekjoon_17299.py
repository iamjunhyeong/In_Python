#NO.17299 오등큰수
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))
stack = []
lenth = {}
for i in seq:
    if i not in lenth:
        lenth[i] = 1
    else:
        lenth[i] += 1

for i in range(n):
    while(stack):
        if lenth[seq[i]] > lenth[seq[stack[-1]]]:
            seq[stack.pop()] = seq[i]
        else:
            stack.append(i)
            break
    
    if not stack:
        stack.append(i)
        
for i in stack:
    seq[i] = -1
    
print(*seq)