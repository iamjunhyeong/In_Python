#NO.1016 제곱ㄴㄴ수
#https://my-coding-notes.tistory.com/86
minn, maxx = map(int,input().split())
#max값을 넘지않는 제곱인 수를 a에 저장
a = [i**2 for i in range(2,int(maxx**0.5)+1)]
num = [1] * (maxx-minn+1)
for i in a:
    n = minn//i*i
    while(n < maxx+1):
        if n - minn >= 0:   #n값이 범위안에 들면
            num[n-minn] = 0
        n += i
print(sum(num))