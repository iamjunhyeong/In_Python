#NO.1700 멀티탭 스케줄링
import sys 
input = sys.stdin.readline

n, k = map(int,input().split())
li = list(map(int,input().split()))


plug = []
cnt = 0
for i in range(k):
    # 이미 플러그가 꽂혀있다면 스킵
    if li[i] in plug:
        continue
    
    # 플러그가 비어있다면 꽂기
    if len(plug) < n:
        plug.append(li[i])
    #### 헷갈렸던 부분 
    # 플러그가 꽉차있다면 다음 물건 순서를 찾아서 가장 
    # 늦게 나오는 물건의 플러그를 뺀다
    else:
        maxx = [0] * len(plug)
        for j in range(len(plug)):
            ind = 0
            for k in li[i:]:
                if plug[j] == k:
                    maxx[j] = ind
                    break
                ind += 1
            else:
                maxx[j] = 101
        plug.pop(maxx.index(max(maxx)))
        plug.append(li[i])
        cnt += 1

print(cnt)