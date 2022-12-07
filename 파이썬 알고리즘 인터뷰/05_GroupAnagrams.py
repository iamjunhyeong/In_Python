li = ["eat","tea","tan","ate","nat","bat"]
dic = {}

for i in li:
    s = ''.join(sorted(i))
    dic[s] = dic.get(s,[]) + [i]  # dic.get(s,[]) key s가 있으면 s의 value값 넣음, 없으면 [] 넣음

for i in dic:
    print(dic[i])    
    