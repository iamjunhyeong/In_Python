import sys
# No. 10828 스택
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push': stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif order[0] == 'size': print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif order[0] == 'top': 
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack[-1])