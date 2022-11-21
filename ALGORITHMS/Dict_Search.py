li = ["Tom","Jerry","Mike","Tom","Mike"]
dic = {}
for i in li:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    
for i in dic:
    if dic[i] > 1:
        print(i)


