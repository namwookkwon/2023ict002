num = int(input())
k=list(map(int,input().split()))
count  = int(input())

cnt=[0]*201

for i in k:
 cnt[i]+=1


print(cnt[count])
