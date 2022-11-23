# No.9020 골드바흐의 추측

def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()


# # No.9020
# def isPrime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     else:
#         return True

# value = list(range(2,10001))
# prime = []
# for i in value:
#     if isPrime(i):
#         prime.append(i)

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     a = n//2
#     b = a
#     for _ in range(10000):
#         if a in prime and b in prime:
#             print(a,b)
#             break
#         a -= 1
#         b += 1
# print()