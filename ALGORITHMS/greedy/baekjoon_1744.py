#NO.1744 수 묶기
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort(reverse=True)
cnt = 0
while li:   
    if len(li) == 1:    # 리스트 하나 남으면 그냥 더하기
        cnt += li.pop()
        break
    if li[-2] <= 0 and li[-1] <= 0: # 리스트 중 0 이하가 두개이상이면 서로 묶기
        a = li.pop()
        b = li.pop()
        cnt += a*b
        continue
    a = li.pop(0)
    b = li.pop(0)
    if a+b >= a*b:  # 1이상 리스트끼리 묶기 or 안묶기 중 고르기
        cnt += a+b
    else: 
        cnt += a*b
print(cnt)
