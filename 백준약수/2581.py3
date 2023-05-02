M=int(input())
N=int(input())
kk=[]

for a in range(M,N+1):
    check=True
    if a==1:
        continue
    for b in range(2,a):
        if a%b==0:
           check=False
           break
        

    if check:
       kk.append(a)

       
if len(kk)==0:
    print(-1)
else:
    print(sum(kk))
    print(min(kk))
