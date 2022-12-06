import timeit
n = list(input())

start_time = timeit.default_timer()

for i in range(len(n)//2): n[i], n[len(n)-1-i] = n[len(n)-1-i], n[i]
print(n)

print(timeit.default_timer()-start_time)

# n = n[::-1] (X) - 공간복잡도
# n.reverse() (O)