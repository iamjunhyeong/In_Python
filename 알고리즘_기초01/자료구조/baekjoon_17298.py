#NO. 17298 오큰수 
n = int(input())
seq = list(map(int,input().split()))
stack = []

for i in range(n):
    while(stack):
        print(seq,stack)
        if seq[i] > seq[stack[-1]]:
            seq[stack.pop()] = seq[i]
        else:
            stack.append(i)
            break
    
    if not stack:
        stack.append(i)
        
print(seq,stack)
for i in stack:
    seq[i] = -1
    
print(*seq)