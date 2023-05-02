num = int(input())

a=[]


for i in range(1,num+1):
  string=input()
  a.append(string[0]+string[-1])

for k in a:
  print(k)