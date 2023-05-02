N,M =map(int,input().split())
cnt=[0]*N

for x in range(M):
  i,j,k=map(int,input().split()) 
  for y in range(i-1,j):
          cnt[y]=k

for z in cnt:
  print(z,end=" ")