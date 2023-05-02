cnt=int(input())
num=list(map(int, input().split()))

count1=0

for a in range(cnt):
    for b in range(2,num[a]):
        if num[a]%b==0:
            count1+=1
            break

    if num[a]==1:
        count1+=1

result=cnt-count1
print(result)