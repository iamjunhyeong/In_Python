while True:
    dic = {1:0,2:0,3:0,4:0}
    s = input()
    for i in s:
        if ord(i) > 96 and ord(i) < 123:
            dic[1] += 1
        elif ord(i) > 64 and ord(i) < 91:
            dic[2] += 1
        elif ord(i) > 47 and ord(i) < 58:
            dic[3] += 1
        else:
            dic[4] += 1

    for i in dic:
        print(dic[i], end=' ')
    print()

# 소문자 대문자 숫자 공백
