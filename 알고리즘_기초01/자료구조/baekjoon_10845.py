# No. 10845 큐
import sys
n = int(sys.stdin.readline())
qu = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push': qu.append(int(order[1]))
    elif order[0] == 'pop':
        if len(qu) == 0: print(-1)
        else: print(qu.pop(0))
    elif order[0] == 'size': print(len(qu))
    elif order[0] == 'empty':
        if len(qu) == 0: print(1)
        else: print(0)
    elif order[0] == 'front': 
        if len(qu) == 0:
            print(-1)
        else: 
            print(qu[0])
    elif order[0] == 'back':
        if len(qu) == 0:
            print(-1)
        else: 
            print(qu[-1])