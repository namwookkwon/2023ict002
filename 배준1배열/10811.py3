N,M= map(int,input().split())
cnt=[i for i in range(1,N+1)]


for a in range(M):
    i,j=map(int,input().split())
    kk=cnt[i-1:j]
    kk.reverse()
    cnt[i-1:j]=kk


for b in cnt:
    print(b,end=" ")

