n=int(input(''))

for i in range(n):
    sum=0
    ch=list(input('').split())

    for j in range(len(ch)):
        if ch[j]=='@':
            sum=sum*3
        elif ch[j]=='%':
            sum=sum+5
        elif ch[j]=='#':
            sum=sum-7
        else:
            sum=sum+float(ch[j])

    print('%.2f'%sum)