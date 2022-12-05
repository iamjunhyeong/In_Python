# ANS 1
from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin :
    if line[0] == 'L' :
        if stk1 : stk2.append(stk1.pop())
        else : continue
    elif line[0] == 'D' :
        if stk2 : stk1.append(stk2.pop())
        else : continue
    elif line[0] == 'B' :
        if stk1 : stk1.pop()
        else : continue
    elif line[0] == 'P' :
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))

# ANS 2
import sys
input = sys.stdin.readline
s = list(input().rstrip())
c = []

for _ in range(int(input())):
    command = input().rstrip()
    if command == "L":
        if s:
            c.append(s.pop())
    elif command == "D":
        if c:
            s.append(c.pop())
    elif command == "B":
        if s:
            s.pop()
    else:
        _,b = command.split()
        s.append(b)
s += c[::-1]
print(*s,sep="")
