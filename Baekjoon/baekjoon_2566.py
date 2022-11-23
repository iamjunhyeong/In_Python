#NO.2566 최댓값
import sys
max,x,y = -1,0,0

for i in range(9):
    li = list(map(int,sys.stdin.readline().split()))
    for j in range(9):
        if li[j] > max :
            max, x, y = li[j],i,j 

print(max)
print(x+1, y+1)