# No. 1158 요세푸스 문제
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
li = [i for i in range(1,n+1)]
st = []
i = 0
while li:
    i = (i+(k-1)) % len(li)
    st.append(li.pop(i))
    
print("<%s>" % (", ".join(map(str,st))))
