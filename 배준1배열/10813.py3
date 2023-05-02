n,m = map(int , input().split())
t=0
count = [i for i in range(1,n+1)]

for k in range(m):
   i,j=map(int, input().split())
   i-=1
   j-=1
   t=count[i]
   count[i]=count[j]
   count[j]=t

for i in range(n):
  print(count[i],end=" ")