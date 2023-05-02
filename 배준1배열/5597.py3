count=[0]*31

for i in  range(1,29):
  k=int(input())
  count[k]=1

for i in range(30):
  if count[i+1]==0:
     print(i+1)