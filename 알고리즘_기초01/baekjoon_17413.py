# NO.17413 단어 뒤집기  2
import sys
input = sys.stdin.readline

S = input().rstrip()    # 개행문자 제거
a = []                  # 결과         
word = ''               # 뒤집을 단어
tag = ''                # 태그된 단어
t = 0                   # 0 = 단어 / 1 = 태그

for i in range(len(S)):
    if S[i] == '<':         #개행 문자 시작
        t = 1
        if len(word):
            a.append(word[::-1])
            word = ''
    elif i != 0 and S[i-1] == '>':  # 개행문자 끝
        t = 0
        if len(tag):
            a.append(tag)
            tag = ''
    elif S[i] == ' ':               # 공백일때
        if len(word):
            a.append(word[::-1])
            word = ''
        if len(tag):
            a.append(tag)
            tag = ''
        a.append(' ')
        continue
    if t == 0: 
        word += S[i]
    elif t == 1:
        tag += S[i]

# 마지막 단어 붙이기
if len(word):
    a.append(word[::-1])
    word = ''
if len(tag):
    a.append(tag)

print(''.join(a))