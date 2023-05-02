num=int(input())
kk=list(map(int,input().split()))
sum=0
M=max(kk)

for i in range(num):
  sum+=(kk[i]/M)*100


total=sum/num

print(total)