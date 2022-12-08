# NO.10820 문자열 분석
while True:
    try:
        dic = {'lower':0,'upper':0,'num':0,'blank':0}
        s = input()
        for i in s:
            if ord(i) > 96 and ord(i) < 123:
                dic['lower'] += 1
            elif ord(i) > 64 and ord(i) < 91:
                dic['upper'] += 1
            elif ord(i) > 47 and ord(i) < 58:
                dic['num'] += 1
            else:
                dic['blank'] += 1

        for i in dic:
            print(dic[i], end=' ')
        print()
    except EOFError:
        break

# 보통 문제에서 입력값의 개수, 즉 T(테스트케이스)가 주어지는데 
# 이 문제는 안 주어짐을 깨닫고 while문으로 무한 루프를 돌리며 
# EOFError인 상황만 제외하고는 반복문이 돌아가도록 하였다.
