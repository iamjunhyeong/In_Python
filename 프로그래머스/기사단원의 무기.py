def count_factor(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): 
        if n%i == 0:
            if i == n//i: 
                cnt += 1
            else:
                cnt += 2 
        if cnt > limit:  
            return power 
    return cnt

def solution(number, limit, power):
    knights = [i for i in range(1,number+1)]
    res = 0
    
    for i in range(number):
        s = count_factor(knights[i], limit, power)
        res += s

    return res
print(solution(5,3,2))
print(solution(10,3,2))
