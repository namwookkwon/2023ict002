N,k=map(int,input().split())
num=[1]
kk=True
for i in range(1,N):
    if N%i==0:
        num.append(N//i)
     
    elif N%i!=0:
         kk=False
        
num.sort()
if k==1:
  print("1")

elif kk==False and k!=0 and len(num)<k:
  print("0")

elif len(num)>=2 :
   print(num[k-1])
  