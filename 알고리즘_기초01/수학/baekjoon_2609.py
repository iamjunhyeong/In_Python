#NO.2609 최대공약수와 최대공배수

a, b = map(int,input().split())
i = 1
j = 1

def Min(a,b,i,j):
    while a/i != b/j:
        if a/i > b/j:
            i += 1
        else:
            j += 1
    return int(a/i)

def Max(a,b,i,j):
    while a*i != b*j:
        if a*i > b*j:
            j += 1
        elif a*i < b*j:
            i += 1
    return a*i

print(Min(a,b,i,j))
print(Max(a,b,i,j))

# :: short ::
# m, n = map(int, input().split())

# def gcd(x, y):
#     if(y==0):
#         return x
#     else:
#         return gcd(y,x%y)

# print(gcd(m,n))               
# print(int(m*n/gcd(m,n)))      # (두 값의 곲) / (최대 공약수)