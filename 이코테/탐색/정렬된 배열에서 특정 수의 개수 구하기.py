# 이진탐색 라이브러리 
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, x = map(int,input().split())
li = list(map(int,input().split()))
print(len(li[bisect_left(li,x):bisect_right(li,x)]))