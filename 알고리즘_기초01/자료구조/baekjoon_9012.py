# No.9012 괄호
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    D = sys.stdin.readline()
    cnt = 0
    for i in D:
        if i == "(": cnt += 1
        elif i == ")": cnt -= 1
        if cnt < 0: break
    if cnt != 0: print("NO")
    else: print("YES")
