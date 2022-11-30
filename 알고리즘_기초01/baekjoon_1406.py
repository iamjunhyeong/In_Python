# NO. 1406 에디터 <시간초과>
import sys 
input = sys.stdin.readline

word = input()
n = int(input())
curser = len(word)-1

for i in range(n):
    a = input().split()
    if a[0] == 'L':
        if curser > 0: curser -= 1
    elif a[0] == 'D':
        if curser < len(word)-1: curser += 1
    elif a[0] == 'B':
        if curser > 0: 
            word = word[:curser-1] + word[curser:]
            curser -= 1
    elif a[0] == 'P':
        word = word[:curser] + a[1] + word[curser:]
        curser += 1
print(word)
