num=int(input())

for i in range(1,num+1):
  a,b=input().split()
  a=int(a)
  
  for k in range(len(b)):
    print(a*b[k],end="")
    
  print()