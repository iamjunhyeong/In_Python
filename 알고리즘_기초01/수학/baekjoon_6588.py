# NO.6588 골드바흐의 추측
import sys
input = sys.stdin.readline
B = 1000000

L=[True for i in range(B+1)]
L[0]=False
L[1]=False
j = 2

for i in range(2,int(B**0.5)+1):
    while 1:
        if i*j <= B:
            L[i*j] = False
            j += 1
        else:
            j = 2
            break

while True:
    n = int(input())
    if n == 0: break

    for i in range(3, len(L)):
        if L[i] and L[n-i]:
            print(f"{n} = {i} + {n-i}")
            break



# import sys
# input=sys.stdin.readline

# #에라토스테네스의 체
# l = [True for i in range(1000001)] #전체 수 만큼 True의 리스트를 생성
# #2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False
# for i in range(2, 1001):    #int(math.sqrt(n)) + 1    
#     if l[i]:
#         for j in range(i + i, 1000001, i):
#             l[j] = False        
# #->소수만 True로 남음
            
# while True:
#     n = int(input())

#     if n == 0: break

#     for i in range(3, len(l)):
#         if l[i] and l[n-i]:    #둘 다 리스트에 있으면
#             print(n, "=", i, "+", n-i)
#             break