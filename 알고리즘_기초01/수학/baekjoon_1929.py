#NO.1929 소수찾기 
A,B=map(int,input().split())

L=[True for i in range(B+1)]
L[0]=False
L[1]=False
j=2

for i in range(2,int(B**0.5)+1):
    while 1:
        if i*j<=B:
            L[i*j]=False
            j+=1
        else:
            j=2
            break

for i in range(A,B+1):
    if L[i]==True:
        print(i)